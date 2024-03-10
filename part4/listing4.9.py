import asyncio
import aiohttp

from async_learn.utils import async_timed, fetch_status_delay


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status_delay(session, 'https://example.com', 1),
                    fetch_status_delay(session, 'https://example.com', 10),
                    fetch_status_delay(session, 'https://example.com', 10)]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')

            for task in asyncio.tasks.all_tasks():
                print(task)


asyncio.run(main())
