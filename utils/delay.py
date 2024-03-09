import asyncio

from .async_timer import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"сон в течение {delay_seconds} с закончился")
    return delay_seconds
