from asyncio import Future
import asyncio

from utils import delay


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(6)
    future.set_result(42)
    print("Значение установлено")


async def main():
    future = make_request()
    print(f"Будущий объект готов? {future.done()}")
    task = asyncio.create_task(delay(5))

    value = await future
    await task
    print(f"Будущий объект готов? {future.done()}")
    print(value)


asyncio.run(main())
