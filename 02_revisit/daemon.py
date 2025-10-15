import threading
import time

def foo():
    while True:
        print('calling foo ...')
        time.sleep(2)

t = threading.Thread(target=foo, daemon= True) # daemon
#t = threading.Thread(target=foo) # non-daemon

t.start()