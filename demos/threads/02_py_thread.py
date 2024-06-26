"""py thread"""

import time
import threading


def some_task() -> None:
    """some task"""

    print("task name: " + threading.current_thread().name)
    print("start some task: " + str(threading.get_native_id()))
    time.sleep(2)
    print("end some task: " + str(threading.get_native_id()))


print("main thread name: " + threading.current_thread().name)
print("start main thread: " + str(threading.get_native_id()))

thread1 = threading.Thread(target=some_task, name="threadA")
thread1.start()

thread2 = threading.Thread(target=some_task, name="threadB")
thread2.start()

thread1.join()
thread2.join()

print("end main thread: " + str(threading.get_native_id()))
