import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='root')

    query = 'SELECT product_id, product_name FROM product'

    count = 0

    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
            count += 1

    print(f'Fetched {count} products')
    await connection.close()


asyncio.run(main())
