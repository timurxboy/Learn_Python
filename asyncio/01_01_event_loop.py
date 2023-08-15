import asyncio
import time

from multithreading.decorators import measure_time, async_measure_time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print("loop is still running")


async def main():
    awaitble_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitble_obj


if __name__ == '__main__':
    # coroutine - main()
    # print(coroutine)

    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
        # loop.run_until_complete(main())
        print("coroutines have finished")
    finally:
        loop.close()
        print("loop is closed")
        print(f"loop is closed = {loop.is_closed()}")