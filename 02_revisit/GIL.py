
import threading as th

# this is similar to Mutex in rust

def foo():
    print(f"{th.current_thread().name} is started")
    i = 0
    for i in range(1, 100_00):
        i += 1
    print(f"{th.current_thread().name} ended task")

thread_1 = th.Thread(target=foo, name="thread_1")
thread_2 = th.Thread(target=foo, name="thread_1")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()


