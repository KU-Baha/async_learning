import asyncio

from async_learn.utils import async_timed, delay

# Old example
# async def main() -> None:
#     task_one = asyncio.create_task(delay(1))
#     task_two = asyncio.create_task(delay(2))
#     await task_one
#     await task_two
#

# If we want more task than 2, we want to use for loop
# Wrong example


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

asyncio.run(main())

# We wait this 3 task will be done in 3 second, but in fact it will be done in 9 second
# The reason why it took 9 second is because we await each task one by one

# Correct example in listing4.5.py
