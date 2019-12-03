# Imports
from multiprocessing import Manager
from multiprocessing import Process
from imutils.video import VideoStream
from facetracker import ObjCenter
from PIDcontroller import PID
import pantilthat as pth
import argparse
import signal
import time
import sys
import cv2
import os
# import pigpio
import RPi.GPIO as GPIO
import lcd_i2c

# our imports
from time import gmtime, strftime
from basic_predictor import predictOnImage
from music_handler import music_handler
from multiprocessing import Lock

# global variables
button_pin1 = 25
button_pin2 = 25
buzzer_pin1 = 27


# The main function for this program is actually at the bottom of the script and labelled "if __name__ == "__main__":"
# The main values of interest for tuning are around line 170, which would are for the PID controller. To add code for
# when the servos move, one should edit pid_process (line 83) as it is the part of the program that informs the servos
# when it needs to change positions, whereas set_servo is always running to keep the servo at the same angle.
# You can read the other functions and likewise the other scripts for a better idea of how this works but there is nothing really to modify there.


def setupLCD():
    lcd_i2c.lcd_init();


def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)


# Define the range for the servos and for convenience which GPIO pins are in use (GPIO label, panning servo first.).
servoRange = (-90, 90)


# This is where the program closes.
# Purpose is to exit the script if necessary, but since this script uses references to multiple different classes, and multiple
# processes running at once (meaning we are running 4 things at once to track faces) and we need to close all of them at once. so we
# call this function in each process.

def signal_handler(sig, frame):
    print("[INFO] 'ctrl + c' pressed, stopping.")

    GPIO.cleanup()

    # exit the program
    sys.exit()


# Calls the facetracker script to find the center of an object.
def print_LCD(str1, str2, classify):
    """Written by Anthony Luo
    """
    while True:
        if GPIO.input(button_pin2) == GPIO.HIGH:
            music_handler(1)  # we check for this here, because music_handler is tied directly to print LCD
            processPrintLCD.terminate()
            exit()
        elif classify:
            str1.value = 'Detected:'
            # classification strings will happen here
        else:
            atime = str(strftime("%m/%d %H:%M:%S", gmtime()))
            str1.value = atime
        printLCD(str1.value, str2.value)
    exit()


def classifier(path, classify, str1, str2, lock):
    """Written by Anthony Luo
    """
    classes = {0: 'Anni', 1: 'Mitch', 2: 'Prey', 3: 'Vitoria'}
    while True:
        if classify:
            lock.acquire()
            face_class = predictOnImage(path.value)
            str2.value = classes[face_class]
            lock.release()
        else:
            time.sleep(1)
            # updates every second or so (not super critical - image is saved anyways)


def obj_center(args, objX, objY, centerX, centerY, lock, classify, path, str1, str2):
    # Uses the signal_handler to stop the program when a keyboard interrupt is made (ctrl + c in terminal)
    signal.signal(signal.SIGINT, signal_handler)

    # Start the video stream and wait for the camera to warm up
    vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    # Initialize the facetracker to report the center of any face on screen
    obj = ObjCenter(args["cascade"])

    while True:
        # print(atime)
        # Grab the frame from the threaded video stream and flip it vertically (since our camera is by default upside down)
        frame = vs.read()
        frame = cv2.flip(frame, 0)
        crop = frame.copy()
        main = frame.copy()

        # Calculate the center of the frame as this is where we will try to keep the face.
        (H, W) = frame.shape[:2]
        centerX.value = W // 2
        centerY.value = H // 2

        # Find the object's location
        objectLoc = obj.update(frame, (centerX.value, centerY.value))
        ((objX.value, objY.value), rect) = objectLoc

        # this handles everything if we want to take a picture

        # Draw a box around the location. A lot of capturing is also handled below.
        if rect is not None:
            str2.value = 'Face Detected'
            (x, y, w, h) = rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # this must happen inline because it can onyl occur when a face is captured.
            if (GPIO.input(button_pin1) == GPIO.HIGH):
                lock.acquire()

                str1.value = 'Taking Picture'
                str2.value = 'Processing...'

                scale_x = abs(w - x) * 0.1
                scale_y = abs(h - y) * 0.5

                y = int(y - scale_y)
                h = int(h + 2 * scale_y)
                x = int(x - scale_x)
                w = int(w + 2 * scale_x)
                crop = crop[y:y + h, x:x + h]
                cv2.imshow('memes.jpg', crop)
                sy, sx = crop.shape[:2]
                dim = sy * 10, sx * 10
                crop = cv2.resize(crop, dim, interpolation=cv2.INTER_AREA)
                ctime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                path.value = ctime + '.png'
                cv2.imshow(path.value, crop)
                cv2.imwrite(path.value, main)
                cv2.imshow(ctime + 'meme', frame)
                lock.release()
                classify.value = True

        # Display the frame to the screen, will create a window named "Pan-Tilt Tracker".
        cv2.imshow("Pan-Tilt Tracker", frame)
        cv2.waitKey(1)

        classify.value = False


# This function handles what is called the PID controller script, which the student will be tuning,
# The actual tuning however happens far below this block, which simply passes values to the other script, or in the movement function.

def pid_process(output, p, i, d, objCoord, centerCoord):
    # Signal trap
    signal.signal(signal.SIGINT, signal_handler)  # Signal

    # Create a PID object (using the PIDcontroller.py script) and initialize it with parameters p, i, and d.
    p = PID(p.value, i.value, d.value)
    p.initialize()

    GPIO.output(21, GPIO.LOW)

    while True:
        # Find the exact error between face center and center of screen, then update the value of error for all processes.
        error = centerCoord.value - objCoord.value  # objCoord.value - centerCoord.value
        output.value = p.update(error)
        # print('center val:', centerCoord.value, 'obj val:', objCoord.value, 'error:', error, sep = ' ') #This tells us what the calculated error is every iteration


# A quick function to compare 1 number to a range of numbers.

def in_range(val, start, end):
    return (val >= start and val <= end)


# This is where the servos are actually told to move, using pan and tilt angles determined by error calculations in the PIDcontroller
# and the angle_converter.
def set_servos(pan, tlt):
    signal.signal(signal.SIGINT, signal_handler)

    while True:

        # The pan and tilt angles are the reverse of the values generated due to the camera being upside down by default.
        # If the servo in use is able to keep the camera right-side-up just remove the -1 from these lines.
        panAngle = (-1) * pan.value
        tiltAngle = (-1) * tlt.value

        # If the pan angle is within the range defined at the top of the script, use the convert_angle function to move towards it.
        if in_range(panAngle, servoRange[0], servoRange[1]):
            try:
                pth.pan(panAngle)
                # print(panAngle)
            except:
                print("Could not move the panning servo.")

        # If the tilt angle is within the range defined at the top of the script, use the convert_angle function to move towards it.
        if in_range(tiltAngle, servoRange[0], servoRange[1]):
            try:
                pth.tilt(tiltAngle)
                # print(tiltAngle)
            except:
                print("Could not move the tilting servo.")


# Check if this is the main body of execution if so, we get to actually start doing stuff.
if __name__ == "__main__":

    # Setup area:

    # This is for running the program from the terminal, allowing us to pass which haarcascade (the package that can actually detect objects)
    # we are using. We pass in "haarcascade_frontalface_default.xml" when running the program as it finds human faces from the front.
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--cascade", type=str, required=True,
                    help="haarcascade_frontalface_default.xml")
    args = vars(ap.parse_args())

    # Start a manager for process-safe variables, this manager allows us to share values between different simultaneous processes, so the process
    # finding the center of a face can pass that value to the PID controller to find error which can pass that value over to move the servos in both
    # the panning process and the tilting process.

    # Anything you want to add on startup (such as setting up GPIO) should be here.

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(buzzer_pin1, GPIO.OUT)
    setupLCD()

    with Manager() as manager:

        # After this the main loop of the program begins, running multiple processes at once which is kind of like if it looped over
        # All of the prior functions at once, so if you want something to loop put it in one of the prior functions.

        # Do not modify these.
        # Don't do it.

        # Set integer values for the object center (x, y)-coords
        centerX = manager.Value("i", 0)
        centerY = manager.Value("i", 0)

        # Set integer values for the object's (x, y)-coords
        objX = manager.Value("i", 0)
        objY = manager.Value("i", 0)

        # Pan and tilt values will be managed by independent PIDs
        pan = manager.Value("i", 0)
        tlt = manager.Value("i", 0)

        # Modify these 6 values, keeping them above 0 and less than 1.
        # These are the coefficients for the PID controller, which modifies the weight that each
        # type of error holds, changing these will modify how the pan-tilt module responds to movement
        # Try adjusting these one at a time to get a feel for how these work.

        # PID values for panning
        panP = manager.Value("f", 0.009)
        panI = manager.Value("f", 0.30)
        panD = manager.Value("f", 0.0005)  # Try to keep these an order of magnitude lower than your P and I values

        # PID values for tilting
        tiltP = manager.Value("f", 0.009)
        tiltI = manager.Value("f", 0.30)
        tiltD = manager.Value("f", 0.0005)  # Try to keep these an order of magnitude lower than your P and I values

        # Values added by L2-4
        classify = manager.Value('b', False)
        path = manager.Value('s', 'new_image.jpg')
        str1 = manager.Value('s', 'Initializing')
        str2 = manager.Value('s', 'Be Patient')

        # Beyond this point is multiprocessing stuff that is not important to know for making this work.

        # Have to deal with four processes now, all at once.
        # objectCenter - find face and how far i it is from center
        # panning      - determines right X coords to pan to
        # tilting      - determines right Y coords to tilt to
        # setServos    - moves the servos

        lock = Lock()
        # TODO: add processes for music, and wtv else.

        processPrintLCD = Process(target=print_LCD, args=(str1, str2))

        processClassifier = Process(target=classifier, args=(path, classify, str1, str2, lock))

        # Declare processes for everything that needs to happen, first passing in the target function to use from above,
        # and passing in the values from the Manager as arguments for the functions. Now they all know which variables to act on together.

        processObjectCenter = Process(target=obj_center,
                                      args=(args, objX, objY, centerX, centerY, lock, classify, path, str1, str2))

        processPanning = Process(target=pid_process, args=(pan, panP, panI, panD, objX, centerX))

        processTilting = Process(target=pid_process, args=(tlt, tiltP, tiltI, tiltD, objY, centerY))

        processSetServos = Process(target=set_servos, args=(pan, tlt))

        # Edited by Anthony Luo: Starts all the processes. Hopefully doesn't set the pi on fire.

        try:
            processObjectCenter.start()
        except:
            print("Failed to start the Object Center process.")

        try:
            processPanning.start()
        except:
            print("Failed to start the panning process.")

        try:
            processTilting.start()
        except:
            print("Failed to start the tilting process.")

        try:
            processSetServos.start()
        except:
            print("Failed to start the set servos process.")

        try:
            processPrintLCD.start()
        except:
            print('Failed to start LCD services')

        try:
            processClassifier.start()
        except:
            print('Failed to start Classifier')

        # Join all 4 processes so they happen together.
        try:
            processObjectCenter.join()
        except:
            print("Could not join Object Center")

        try:
            processPanning.join()
        except:
            print("Could not join Panning")

        try:
            processTilting.join()
        except:
            print("Could not join Tilting")

        try:
            processSetServos.join()
        except:
            print("Could not join Set Servos")

        try:
            processPrintLCD.join()
        except:
            print('could not join LCD printing')

        try:
            processClassifier.join()
        except:
            print('Could not join LCD Printer')
