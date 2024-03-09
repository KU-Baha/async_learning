import asyncio
import multiprocessing as mp
from time import time

from async_learn.utils import async_timed, delay


def cpu_bound_work() -> int:
    counter = 0

    for i in range(100000000):
        counter = counter + 1

    return counter


def main():
    start_time = time()

    task_one = mp.Process(target=cpu_bound_work)
    task_two = mp.Process(target=cpu_bound_work)

    task_one.start()
    task_two.start()

    task_one.join()
    task_two.join()

    end_time = time()
    print(f"Время выполнения: {end_time - start_time}")


if __name__ == "__main__":
    main()
