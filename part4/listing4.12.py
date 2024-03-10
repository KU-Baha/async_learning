import aiohttp
import asyncio
import loguru

from async_learn.utils import async_timed, fetch_status_delay

loguru.logger.add('async_learn.log', format="{time} {level} {message}", level="INFO")


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status_delay(session, 'python://bad.com')),
                    asyncio.create_task(fetch_status_delay(session, 'https://www.example.com', delay=3)),
                    asyncio.create_task(fetch_status_delay(session, 'https://www.example.com', delay=3))
                    ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                loguru.logger.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())

        for pending_task in pending:
            loguru.logger.warning(f'Отменяем ожидающую задачу {pending_task}')
            pending_task.cancel()


asyncio.run(main())
