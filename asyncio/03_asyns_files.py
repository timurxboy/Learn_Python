import asyncio

import aiofiles as aiofiles


def read_lange_file():
    with open('big_file.txt', 'r') as f:
        return f.read()


async def async_read_lange_file():
    async with aiofiles.open('big_file.txt', 'r') as f:
        return await f.read()


def count_words(text):
    return len(text.split(' '))


async def async_main():
    text = await async_read_lange_file()
    print(count_words(text))

def main():
    text = read_lange_file()
    print(count_words(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    main()
