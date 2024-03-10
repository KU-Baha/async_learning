import asyncio
import aiohttp
import loguru

from async_learn.utils import async_timed, fetch_status

loguru.logger.add('async_learn.log', format="{time} {level} {message}", level="INFO")


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [asyncio.create_task(good_request), asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                loguru.logger.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())


asyncio.run(main())
