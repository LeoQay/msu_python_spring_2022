import unittest
import fetcher
import asyncio


class TestFetcher(unittest.TestCase):
    def test_1(self):
        args = {'c': 10, 'urls': 'files/not_existed.txt'}
        result = asyncio.run(fetcher.main(args))
        self.assertEqual(len(result), 0)

    def test_2(self):
        args = {'c': 5, 'urls': 'files/for_test_2.txt'}
        result = asyncio.run(fetcher.main(args))
        self.assertEqual(len(result), 0)

    def test_3(self):
        args = {'c': 15, 'urls': 'files/for_test_3.txt'}
        result = asyncio.run(fetcher.main(args))
        self.assertEqual(len(result), 1)
        res = {
            "https://web.archive.org/web/20210729085751/": {
                "of": 19,
                "icon": 15,
                "An": 14,
                "a": 13,
                "illustration": 13
            }
        }
        self.assertEqual(result, res)

    def test_4(self):
        args = {'c': 15, 'urls': 'files/for_test_4.txt'}
        result = asyncio.run(fetcher.main(args))
        res = {
            "https://archive.today/20170601123918/": {
                "Not": 1,
                "Found": 1
            },
            "https://web.archive.org/web/20210729085751/": {
                "of": 19,
                "icon": 15,
                "An": 14,
                "a": 13,
                "illustration": 13
            }
        }
        self.assertEqual(result, res)


if __name__ == "__main__":
    unittest.main()
