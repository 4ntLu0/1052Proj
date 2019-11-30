from multiprocessing import Manager, Process, Lock


def play_original(has_moved):
    """
    Written by Anthony Luo
    """
    # plays the hot cross buns theme
    while True:
        if has_moved:
            play_new()
            exit()
        else:
            continue


def play_new():
    """
    Written by Anthony Luo
    Plays the spongebob theme.
    """


def Handler():
    with Manager() as manager:
        has_moved = manager.Value('b', False)
