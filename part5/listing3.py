import asyncio

import asyncpg

from async_learn.part5.listing2 import CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE, \
    CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='root'
    )

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    ]

    print('Создается база данных product...')

    for statement in statements:
        status = await connection.execute(statement)
        print(status)

    print('База данных product создана!')
    await connection.close()


asyncio.run(main())
