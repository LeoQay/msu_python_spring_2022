import multiprocessing
import os
import unittest
import server as sv
import client as cl


class Testing(unittest.TestCase):
    def check_file_empty(self, file_name):
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip() != '':
                    self.assertTrue(False)

    def test_1(self):
        """
        with empty file of urls
        """
        server_file = 'server_test_1.txt'
        client_file = 'client_test_1.txt'

        server = multiprocessing.Process(
            target=sv.main,
            args=(['server', '-w', '1', '-k', '1'], server_file),
        )

        with open('for_test_1.txt', 'w'):
            pass

        client = multiprocessing.Process(
            target=cl.main,
            args=(['client', '1', 'for_test_1.txt'], client_file)
        )

        server.start()

        client.start()
        client.join()

        server.terminate()

        try:
            self.check_file_empty('server_test_1.txt')
            self.check_file_empty('client_test_1.txt')
        finally:
            os.remove('server_test_1.txt')
            os.remove('client_test_1.txt')
            os.remove('for_test_1.txt')


if __name__ == "__main__":
    unittest.main()
