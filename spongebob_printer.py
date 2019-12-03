
import RPi.GPIO as GPIO
import lcd_i2c
import time

def setupLCD():
    lcd_i2c.lcd_init();


def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2);

def print_all_spongebob():
    printLCD("Are you ready", "kids?")
    time.sleep(1)

    printLCD("Aye-aye,", "Captain")
    time.sleep(1)

    printLCD("I cant hear", "Youuuu")
    time.sleep(1)

    printLCD("Aye-aya,", "captain")
    time.sleep(1)

    printLCD("Ooooooooooooooo", "")
    time.sleep(3)

    mystr = "        Who lives in a Pineapple under the sea?"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.5)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    mystr = "        Absorbent and yellow and porus is he!"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.25)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    mystr = "        If nautical nonsense be something you wish"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.25)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    mystr = "        Then drop on the", "deck and flop like a fish"
    for pos in range(len(mystr)):
        printLCD("mystr[pos:pos+16]", "")
        time.sleep(0.25)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    printLCD("Spongebob", "Squarepants!")
    time.sleep(3)

    printLCD("Spongeboooob", "Squarepaaaaants!")
    time.sleep(3)

    printLCD("Arr harr", " harr harr!")
    time.sleep(3)