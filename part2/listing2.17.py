import asyncio

from async_learn.utils import async_timed, delay


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two


asyncio.run(main())
