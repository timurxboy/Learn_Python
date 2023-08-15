import asyncio

import aiohttp


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.albumId = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnailUrl = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    print('print photo titles')
    for photo in photos:
        print(f"{photo.title}", end="\n")


async def photos_by_album(task_name, album, session):
    print(f"{task_name=}")
    if isinstance(album, int):
        await asyncio.sleep(2)
        raise RuntimeError('Invalid album number')

    url = f"https://jsonplaceholder.typicode.com/photos?albumId={album}/photos/"
    response = await session.get(url)
    photos_json = await response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    await asyncio.sleep(sleeping_period)

    print(f"Finished task={task_name}")
    return [Photo.from_json(photo) for photo in photos_json]


async def main_wait():
    async with aiohttp.ClientSession() as session:
        tasks = [
            photos_by_album('t1', 1, session),
            photos_by_album('t2', 2, session),
            photos_by_album('t3', 3, session),
            photos_by_album('ta', 'a', session),
            photos_by_album('t4', 4, session),
        ]

        photos = []
        done_tasks, pending_tasks = await asyncio.wait(tasks)

        for pending_task in pending_tasks:
            print(f"cancelling {pending_task}")
            print(pending_task.cancel())

        for done in done_tasks:
            try:
                result = done.result()
                photos.extend(result)
            except Exception as ex:
                print(repr(ex))

        print_photo_titles(photos)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(main_wait())
    finally:
        print('Closing loop')
        loop.close()