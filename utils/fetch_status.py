import asyncio

from aiohttp import ClientSession

from async_learn.utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as response:
        return response.status


async def fetch_status_delay(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)

    async with session.get(url) as result:
        return result.status
