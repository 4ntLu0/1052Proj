import RPi.GPIO as GPIO
import lcd_i2c
import time
import numpy

GPIO.setmode(GPIO.BCM)
servoPIN = 22

GPIO.setup(servoPIN, GPIO.OUT)


def setupLCD():
    lcd_i2c.lcd_init();


def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2);


setupLCD()

def print_all_spongebob():
    printLCD("Are you ready", "kids?")
    time.sleep(1)
    time.sleep(1)

    printLCD("Aye-aye,", "Captain")
    time.sleep(1)
    time.sleep(1)

    printLCD("I cant hear", "Youuuu")
    time.sleep(1)
    time.sleep(1)

    printLCD("Aye-aya,", "captain")
    time.sleep(1)
    time.sleep(1)

    printLCD("Ooooooooooooooo", "")
    time.sleep(1)
    time.sleep(1)

    mystr = "        Who lives in a Pineapple under the sea?"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    mystr = "        Absorbent and yellow and porous is he!"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    mystr = "        If nautical nonsense be something you wish"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    mystr = "        Then drop on the", "deck and flop like a fish"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    printLCD("Ready?", "")
    time.sleep(1)
    time.sleep(1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(1)
    time.sleep(1)

    printLCD("Spongeboooob", "Squarepaaaaants!")
    time.sleep(1)
    time.sleep(1)

    printLCD("Arr harr", " harr harr!")
    time.sleep(1)
    time.sleep(1)

