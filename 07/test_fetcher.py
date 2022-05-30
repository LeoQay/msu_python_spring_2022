import unittest
import json, re
import httpretty
import fetcher


class TestFetcher(unittest.IsolatedAsyncioTestCase):
    async def test_1(self):
        args = {'c': 10, 'urls': 'files/not_existed.txt'}
        await fetcher.main(args)

    async def test_2(self):
        with httpretty.enabled(allow_net_connect=True, verbose=True):
            httpretty.register_uri(httpretty.GET,
                                   re.compile(r'http://.*'),
                                   body=json.dumps({'key1': 'value1', 'key2': 'value2'}))

            with open('test_file.txt', 'w') as file:
                print("http://httpretty.example.com", file=file)

            args = {'c': 2, 'urls': 'test_file.txt'}
            await fetcher.main(args)


if __name__ == "__main__":
    unittest.main()
