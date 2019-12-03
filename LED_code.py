import RPi.GPIO as GPIO  # Library for the GPIO Pins
import time  # Library for time-related tasks

GPIO.setmode(GPIO.BCM)  # Sets the way we reference the GPIO Pins
GPIO.setup(25, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(8, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(7, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(1, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(12, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(16, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(11, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(9, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(10, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin
GPIO.setup(20, GPIO.OUT)  # Sets GPIO Pin 25 to an output pin


def Who_lives_in_a_pineapple():  # Who lives in a pineapple under the sea
    # PART 1 OF SONG
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)  # 4
    GPIO.setup(8, GPIO.OUT)  # 5
    GPIO.setup(9, GPIO.OUT)  # 2
    GPIO.setup(11, GPIO.OUT)  # 4
    GPIO.output(25, GPIO.HIGH)  # Low 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(25, GPIO.LOW)  # Low 1

    GPIO.output(8, GPIO.HIGH)  # Mid 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(8, GPIO.LOW)  # Low 1

    GPIO.output(25, GPIO.HIGH)  # High 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(25, GPIO.LOW)  # Low 1

    GPIO.output(11, GPIO.HIGH)  # Mid 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(11, GPIO.LOW)  # Low 1

    GPIO.output(9, GPIO.HIGH)  # Low 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(9, GPIO.LOW)  # Low 1

    GPIO.output(11, GPIO.HIGH)  # Mid 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(11, GPIO.LOW)  # Low 1

    GPIO.output(25, GPIO.HIGH)  # High 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(25, GPIO.LOW)  # Low 1

    GPIO.output(8, GPIO.HIGH)  # Mid 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(8, GPIO.LOW)  # Low 1

    GPIO.output(25, GPIO.HIGH)  # High 1
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(25, GPIO.LOW)  # Low 1

    GPIO.output(11, GPIO.HIGH)  # Mid 2
    time.sleep(1)  # Pauses the program for 1.5 seconds
    GPIO.output(11, GPIO.LOW)  # Low 1


def Yellow_and_Porous():  # Absorbant and Yellow and Porous is he
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1, GPIO.OUT)  # 7
    GPIO.setup(12, GPIO.OUT)  # 8
    GPIO.setup(7, GPIO.OUT)  # 6
    GPIO.setup(8, GPIO.OUT)  # 5
    # PART 2 OF SONG
    GPIO.output(1, GPIO.HIGH)  # Low 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(1, GPIO.LOW)  # Low 2

    GPIO.output(12, GPIO.HIGH)  # Mid 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(12, GPIO.LOW)  # Mid 2

    GPIO.output(1, GPIO.HIGH)  # High 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(1, GPIO.LOW)  # High 2

    GPIO.output(7, GPIO.HIGH)  # Mid 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(7, GPIO.LOW)  # Mid 2

    GPIO.output(8, GPIO.HIGH)  # Low 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(8, GPIO.LOW)  # Low 2

    GPIO.output(7, GPIO.HIGH)  # Mid 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(7, GPIO.LOW)  # Mid 2

    GPIO.output(1, GPIO.HIGH)  # High 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(1, GPIO.LOW)  # High 2

    GPIO.output(12, GPIO.HIGH)  # Mid 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(12, GPIO.LOW)  # Mid 2

    GPIO.output(1, GPIO.HIGH)  # High 2
    time.sleep(0.25)  # Pauses the program for 1 second
    GPIO.output(1, GPIO.LOW)  # High 2

    GPIO.output(7, GPIO.HIGH)  # Mid 2
    time.sleep(1)  # Pauses the program for 1.5 seconds
    GPIO.output(7, GPIO.LOW)  # Mid 2


def SPONGE_BOB():  # Sponge bob square pants
    # Chorus Part of the song
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10, GPIO.OUT)  # 1
    GPIO.setup(9, GPIO.OUT)  # 2
    GPIO.setup(11, GPIO.OUT)  # 3
    GPIO.setup(25, GPIO.OUT)  # 4
    GPIO.setup(8, GPIO.OUT)  # 5
    GPIO.setup(7, GPIO.OUT)  # 6
    GPIO.setup(1, GPIO.OUT)  # 7
    GPIO.setup(12, GPIO.OUT)  # 8
    GPIO.setup(16, GPIO.OUT)  # 9
    GPIO.setup(20, GPIO.OUT)  # 10

    GPIO.output(1, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(1, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)


GPIO.cleanup()  # Resets the GPIO Pins that we used
