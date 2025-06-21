import multiprocessing
import time


def letter():
    for i in "abcd":
        time.sleep(1)
        print(f"letter:{i}")


def number():
    for i in range(5):
        time.sleep(1.5)
        print(f"number:{i}")


if __name__ == "_main_":
    t1 = Process(target=letter)
    t2 = Process(target=number)

    current_time = time.time()
    # start the thread
    t1.start()
    t2.start()
    # wait for thread to complete
    t1.join()
    t2.join()

    used_time = time.time() - current_time
    print(used_time)