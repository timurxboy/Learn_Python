import asyncio


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')
    return 'TIK-TOCK'


async def main():
    t1 = asyncio.create_task(tick(), name='Task1')
    t2 = asyncio.ensure_future(tick())

    # await t1
    # await t2

    results = await asyncio.gather(t1, t2)

    print(f"Task {t1.get_name()}. Done = {t1.done()}")
    print(f"Task {t2.get_name()}. Done = {t2.done()}")

    for x in results:
        print(x)


if __name__ == '__main__':
    asyncio.run(main())