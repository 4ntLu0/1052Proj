from multiprocessing import Manager, Process, Lock
import sys
import time

def myprinter(line1, line2, lock):
    try:
        while(True):
            lock.acquire()
            print(str(line1.value))
            print(str(line2.value))
            time.sleep(2)
            lock.release()
    except KeyboardInterrupt:
        print('stopping')
        sys.exit()

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
        line1 = manager.Value('s', '')
        line2 = manager.Value('s', '')

        processMyPrint = Process(target = myprinter, args = (line1, line2, lock))
        processReadFile = Process(target = readfile, args = (line1, line2, lock))

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