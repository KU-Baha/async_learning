import asyncio
import aiohttp

from async_learn.utils import fetch_status, fetch_status_delay


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.example.com')
        api_b = fetch_status_delay(session, 'https://www.example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            # Никогда не сработает так как задача api_b измениться после wait, будет другой объект
            # Правильно надо было до обернуть в task как в listing4.15.py
            if task is api_b:
                print('API B слишком медленный, отмена')
                task.cancel()


asyncio.run(main())
