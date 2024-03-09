import asyncio
import aiohttp
from aiohttp import ClientSession
from async_learn.utils import async_timed, fetch_status, sync_timed
import requests


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://www.example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        statuses = await asyncio.gather(*requests)
        print(statuses)


# Sync version just for example
@sync_timed()
def main_sync():
    urls = ['https://www.example.com' for _ in range(1000)]
    statuses = [requests.get(url).status_code for url in urls]
    print(statuses)


# Sync version just for example
@async_timed()
async def main_sync_two():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)


if __name__ == '__main__':
    asyncio.run(main())
    # main_sync()
