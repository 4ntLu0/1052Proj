from multiprocessing import Manager, Process
from music_player import play_spongebob_theme,  play_super_mario
from spongebob_printer import print_all_spongebob
from LED_code import Who_lives_in_a_pineapple, Yellow_and_Porous, SPONGE_BOB
import time

def play_original(has_moved):
    """
    Written by Anthony Luo
    """
    while True:
        if has_moved:
            exit()
        else:
            play_super_mario()


def play_new():
    """
    Written by Anthony Luo
    Plays the spongebob theme.
    """
    while True:
        time.sleep(4)
        play_spongebob_theme()

def print_new():
    print_all_spongebob()

def LED_new():
    time.sleep(4)
    SPONGE_BOB()
    Who_lives_in_a_pineapple()
    Yellow_and_Porous()

def handler(mver=0):
    """
    Also written by Anthony Luo, just very badly.
    """
    with Manager() as manager:
        has_moved = manager.Value('b', False)
        processOriginal = Process(target=play_original, args=(has_moved))
        processNew = Process(target=play_new, args=())
        processNewPrinter = Process(target = print_new, args = ())
        processLED = Process(target = LED_new(), args =())
    if mver == 0:
        processOriginal.start()
        processOriginal.join()
    elif mver == 1:
        processOriginal.kill()
        processNew.start()
        processNewPrinter.start()
        processLED.start()
        processNew.join()
        processNewPrinter.join()
        processLED.join()
