import asyncio
from utils import delay


async def main():
    task = asyncio.create_task(delay(5))

    try:
        print("Запуск задачи")
        result = await asyncio.wait_for(asyncio.shield(task), timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Задача заняла более 1 с, скоро она закончится!")
        result = await task
        print(result)


asyncio.run(main())
