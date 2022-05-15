import sys
import aiohttp
import asyncio
import argparse
import json
from bs4 import BeautifulSoup
from collections import Counter


top_k = 5
results = {}


async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, features='html.parser')
            stat = Counter(soup.get_text().split()).most_common(top_k)
            results[url] = {pair[0]: pair[1] for pair in stat}
    except BaseException as e:
        results[url] = str(e)


async def worker(work_queue):
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            await fetch_url(session, url)


async def main(args):
    work_queue = asyncio.Queue()
    with open(args['urls'], 'r') as file:
        for line in file:
            await work_queue.put(line.strip())
    tasks = [asyncio.create_task(worker(work_queue)) for _ in range(args['c'])]
    await asyncio.gather(*tasks)


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', type=str)
    parser.add_argument('-c', type=int, default=10)
    return parser.parse_args(args=argv[1:]).__dict__


if __name__ == '__main__':
    asyncio.run(main(get_args(sys.argv)))
    with open('result.txt', 'w') as file:
        print(json.dumps(results, indent=4), file=file)
