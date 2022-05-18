import multiprocessing
import os
import unittest
from time import sleep
import server as sv
import client as cl


def clear_file(file_name):
    with open(file_name, 'w', encoding='utf-8'):
        pass


class Testing(unittest.TestCase):
    def check_file_content(self, file_name, correct_lines):
        with open(file_name, 'r', encoding='utf-8') as out:
            lines = out.readlines()
        print(lines)
        self.assertEqual(len(lines), len(correct_lines))
        for line, correct in zip(lines, correct_lines):
            self.assertEqual(line.strip(), correct.strip())

    def test_1(self):
        """
        with empty file of urls
        """
        server_file = 'server_test_1.txt'
        client_file = 'client_test_1.txt'
        urls = 'for_test_1.txt'

        server = multiprocessing.Process(
            target=sv.main,
            args=(['server', '-w', '1', '-k', '1', '-a', '9080'], server_file),
        )

        clear_file(client_file)
        clear_file(server_file)
        clear_file(urls)

        client = multiprocessing.Process(
            target=cl.main,
            args=(['client', '1', '-a', '9080', urls], client_file)
        )

        server.start()
        client.start()
        client.join()
        sleep(0.1)
        server.kill()

        try:
            self.check_file_content(server_file, [])
            self.check_file_content(client_file, [])
        finally:
            os.remove(server_file)
            os.remove(client_file)
            os.remove(urls)

    def one_url_test(self, address, url, top, correct):
        server_file = 'server_test.txt'
        client_file = 'client_test.txt'
        urls = 'for_test.txt'

        clear_file(server_file)
        clear_file(client_file)
        with open(urls, 'w', encoding='utf-8') as out:
            print(url, file=out)

        server = multiprocessing.Process(
            target=sv.main,
            args=(['server', '-w', '1', '-k', str(top), '-a', str(address)], server_file),
        )

        client = multiprocessing.Process(
            target=cl.main,
            args=(['client', '1', '-a', str(address), urls], client_file)
        )

        server.start()
        client.start()
        client.join()
        sleep(0.1)
        server.kill()

        try:
            self.check_file_content(server_file, correct['server'])
            self.check_file_content(client_file, correct['client'])
        finally:
            os.remove(client_file)
            os.remove(server_file)
            os.remove(urls)

    def test_2(self):
        self.one_url_test(9081,
                          'https://en.wikipedia.org/wiki/Wikipedia',
                          10,
                          {
                              'server': ['Server: urls processed: 1'],
                              'client': ['https://en.wikipedia.org/wiki/Wikipedia:',
                                         '[["the", 900], ["of", 793], ["and", 475],'
                                         ' ["Wikipedia", 448], ["^", 393], ["to", 383],'
                                         ' ["in", 369], ["a", 364], ["on", 285],'
                                         ' ["Retrieved", 278]]']
                          }
                          )

    def test_3(self):
        self.one_url_test(9082,
                          'https://leetcode.com',
                          3,
                          {
                              'server': ['Server: urls processed: 1'],
                              'client': ['https://leetcode.com:',
                                         '[["|", 5], ["LeetCode", 2], ["-", 1]]', '']
                          }
                          )


if __name__ == "__main__":
    unittest.main()
