import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='root')

    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'

        cursor = await connection.cursor(query)  # A

        await cursor.forward(500)  # B

        products = await cursor.fetch(100)  # C
        count = 0

        for product in products:
            print(product)
            count += 1

        print(f'Fetched {count} products')

    await connection.close()


asyncio.run(main())
