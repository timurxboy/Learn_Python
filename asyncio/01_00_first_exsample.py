import asyncio
import time

from multithreading.decorators import measure_time, async_measure_time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


@async_measure_time
async def main():
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    asyncio.run(main())
