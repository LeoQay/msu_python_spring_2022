import unittest
import asyncio
import fetcher
import httpretty


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_1(self):
        args = {'c': 10, 'urls': 'files/not_existed.txt'}
        await fetcher.main(args)

    async def test_2(self):

        with open('test_file.txt', 'w') as file:
            print('https://address.com/', file=file)

        args = {'c': 2, 'urls': 'test_file.txt'}
        await fetcher.main(args)



if __name__ == "__main__":
    unittest.main()
