"""py thread lock"""

import threading
import time

counter = 0

counter_lock = threading.Lock()


def do_it() -> None:
    """do it"""

    global counter

    print(f"get lock: {threading.get_native_id()}")
    with counter_lock:
        print(f"get counter: {threading.get_native_id()}")
        x = counter
        time.sleep(1)
        print(f"finish sleep: {threading.get_native_id()}")
        x = x + 1
        counter = x


print(f"start counter: {counter}")

thread1 = threading.Thread(target=do_it)
thread1.start()
thread2 = threading.Thread(target=do_it)
thread2.start()

thread1.join()
thread2.join()

print(f"end counter: {counter}")
