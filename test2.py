from test import myprinter
import sys
import os
import time
from multiprocessing import Manager, Process, Lock
def readfile(line1, line2, lock):
    for i in '123456789abcdefghijklmnopqrstuvwxyz':
        lock.acquire()
        print('acquired')
        line1.value = i
        line2.value = i + ' two !'
        time.sleep(0.5)
        lock.release()
        print('released')

if __name__ == '__main__':
    with Manager() as manager:
        lock = Lock()
        l1 = manager.Value('i', 0)
        l2 = manager.Value('i', 0)

        processMyPrint = Process(target = myprinter, args = (l1, l2, lock))
        processReadFile = Process(target = readfile, args = (l1, l2, lock))

        try:
            processMyPrint.start()
            processReadFile.start()
        except:
            print('unable')

        try:
            processMyPrint.join()
            processReadFile.join()
        except:
            print('unable to join')