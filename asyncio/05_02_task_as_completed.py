import asyncio
import time


async def tick():
    await asyncio.sleep(1)
    print('Tick')


async def tock():
    await asyncio.sleep(1)
    print('Tock')

async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task(tick())
    t2 = asyncio.create_task(tock())

    # result = await asyncio.gather(t1, t2)
    # for i, start in enumerate(result, start = 1 ):

    for i, t in enumerate((t1,t2), start=1):
        result = await t
        elapsed = time.perf_counter() - start
        print(f"Executor {i} in {elapsed:0.2f} seconds")


if __name__ == '__main__':
    