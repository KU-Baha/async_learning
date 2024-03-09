import asyncio

from aiogram.client.session import aiohttp

from async_learn.utils import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*tasks)
        print(status_codes)


if __name__ == '__main__':
    asyncio.run(main())
