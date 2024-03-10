import asyncio

from aiogram.client.session import aiohttp

from async_learn.utils import async_timed, fetch_status


# @async_timed()
# async def main():
#     async with aiohttp.ClientSession() as session:
#         urls = ['https://example.com', 'python://example.com']
#         tasks = [fetch_status(session, url) for url in urls]
#         status_codes = await asyncio.gather(*tasks)
#         print(status_codes)

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # exceptions = [res for res in results if isinstance(res, Exception)]
        # successful_results = [res for res in results if not isinstance(res, Exception)]

        exceptions = list(filter(lambda res: isinstance(res, Exception), results))
        successful_results = list(filter(lambda res: not isinstance(res, Exception), results))

        print(f'Все результаты: {results}')
        print(f'Завершились успешно: {successful_results}')
        print(f'Завершились с исключением: {exceptions}')


if __name__ == '__main__':
    asyncio.run(main())
