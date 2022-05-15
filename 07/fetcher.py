import sys
import aiohttp
import asyncio
import argparse
import json
from bs4 import BeautifulSoup
from collections import Counter


top_k = 5


async def fetch_url(session, url, results):
    try:
        async with session.get(url) as response:
            data = await response.text()
            soup = BeautifulSoup(data, features='html.parser')
            stat = Counter(soup.get_text().split()).most_common(top_k)
            results[url] = {pair[0]: pair[1] for pair in stat}
    except BaseException as e:
        results[url] = str(e)


async def worker(work_queue, results):
    async with aiohttp.ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            await fetch_url(session, url, results)


async def main(args):
    results = {}
    work_queue = asyncio.Queue()
    try:
        with open(args['urls'], 'r') as fp:
            for line in fp:
                await work_queue.put(line.strip())
    except BaseException:
        return {}
    tasks = [
        asyncio.create_task(worker(work_queue, results))
        for _ in range(args['c'])
    ]
    await asyncio.gather(*tasks)
    return results


def get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', type=str)
    parser.add_argument('-c', type=int, default=10)
    return parser.parse_args(args=argv[1:]).__dict__


if __name__ == '__main__':
    result = asyncio.run(main(get_args(sys.argv)))
    with open('result.txt', 'w') as file:
        print(json.dumps(result, indent=4), file=file)
