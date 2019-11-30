from multiprocessing import Manager, Process, Lock
from sponge_bob_song import spongebob_theme

def play_original(has_moved):
    """
    Written by Anthony Luo
    """
    while True:
        if has_moved:
            exit()
        else:
            # play hot-cross-buns theme
            # should play sequentially


def play_new():
    """
    Written by Anthony Luo
    Plays the spongebob theme.
    """
    while True:
        spongebob_theme()


def music_handler(mver=0):
    with Manager() as manager:
        has_moved = manager.Value('b', False)
        processOriginal = Process(target=play_original, args=(has_moved))
        processNew = Process(target=play_new, args=())
    if mver == 0:
        processOriginal.start()
        processOriginal.join()
    elif mver == 1:
        processOriginal.kill()
        processNew.start()
        processNew.join()
