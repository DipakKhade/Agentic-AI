
import threading
import time


def task1(task):
    print(f"task 1 started  --{task}")
    time.sleep(1)
    print("task 1 ended")

def task2(task):
    print(f"task 2 started ----{task}")
    time.sleep(5)
    print("task 2 ended")

task1_thread = threading.Thread(target=task1, args=("go to gym",))
task2_thread = threading.Thread(target=task2, args=("go to market",))

task1_thread.start()
task2_thread.start()

task1_thread.join()
task2_thread.join()

print('both thread work is done')

