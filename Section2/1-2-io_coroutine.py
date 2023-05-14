# https://2.python-requests.org/en/master/user/advanced/#id1
# https://docs.aiohttp.org/en/stable/
# pip install aiohttp~=3.7.3

import aiohttp
import time
import asyncio
import os
import threading


async def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://apple.com", "https://google.com"] * 50

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # result = await fetcher(session, urls[0])
        # print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 0.82s
