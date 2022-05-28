import sys
import asyncio
import argparse
from collections import Counter
import aiohttp
from bs4 import BeautifulSoup


async def get_url(file_name):
    with open(file_name, 'r', encoding='utf-8') as urls:
        for url in urls:
            yield url.strip()


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
    except aiohttp.ClientHttpProxyError:
        pass
    except aiohttp.ClientConnectionError:
        pass
    except aiohttp.ClientConnectorError:
        pass
    soup = BeautifulSoup(data, features='html.parser')
    return Counter(soup.get_text().split()).most_common(5)


async def worker(lock, urls):
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with lock:
                    url = await anext(urls)
                stat = await fetch_url(session, url)
                print(stat)
            except StopAsyncIteration:
                return
            except ...:
                pass


async def main(args):
    urls = get_url(args['urls'])
    lock = asyncio.Lock()
    tasks = [
        asyncio.create_task(worker(lock, urls))
        for _ in range(args['c'])
    ]
    await asyncio.gather(*tasks)


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', type=str)
    parser.add_argument('-c', type=int, default=10)
    return parser.parse_args(args=argv[1:]).__dict__


if __name__ == '__main__':
    asyncio.run(main(get_args(sys.argv)))
