import os
import filecmp
import unittest
import html_parser as hp


class TestHtmlParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.test_file_name = ''
        self.validator_name = ''
        self.input_file_name = ''

    def tearDown(self) -> None:
        os.remove(self.test_file_name)
        self.test_file_name = ''
        self.input_file_name = ''
        self.validator_name = ''

    def set_test_name(self, test_name: str):
        self.input_file_name = 'test_files/' + test_name + '/input.txt'
        self.test_file_name = 'test_files/' + test_name + '/output.txt'
        self.validator_name = 'test_files/' + test_name + '/valid.txt'
        with open(self.test_file_name, 'w', encoding='UTF-8') as file:
            file.close()

    def prefix_caller(self, prefix: str):
        def call_f(tok: str):
            with open(self.test_file_name, 'a', encoding='UTF-8') as file:
                print(prefix, tok, sep='', file=file)
        return call_f

    def call_open_tag(self):
        return self.prefix_caller('Open tag:')

    def call_close_tag(self):
        return self.prefix_caller('Close tag:')

    def call_data(self):
        return self.prefix_caller('Data:')

    def get_input_str(self) -> str:
        with open(self.input_file_name, 'r', encoding='UTF-8') as file:
            input_str = ''.join(file)
            file.close()
            return input_str

    def parse_to_file(self, html_str: str):
        hp.parse_html(html_str,
                      self.call_open_tag(),
                      self.call_data(),
                      self.call_close_tag())

    @staticmethod
    def print_open_tag(tok: str):
        print("Open tag:", tok, sep='')

    @staticmethod
    def print_close_tag(tok: str):
        print("Close tag:", tok, sep='')

    @staticmethod
    def print_data(tok: str):
        print("Data:", tok, sep='')

    @staticmethod
    def parse_to_console(html_str: str):
        hp.parse_html(html_str,
                      TestHtmlParser.print_open_tag,
                      TestHtmlParser.print_data,
                      TestHtmlParser.print_close_tag)

    def do_test_input_output(self, test_name: str):
        self.set_test_name(test_name)
        html_str = self.get_input_str()
        self.parse_to_file(html_str)
        is_equal = filecmp.cmp(self.test_file_name, self.validator_name)
        if not is_equal:
            TestHtmlParser.parse_to_console(html_str)
        self.assertTrue(is_equal)

    def test_io_simple(self):
        self.do_test_input_output('simple')

    def test_io_1(self):
        self.do_test_input_output('io1')


if __name__ == '__main__':
    unittest.main()
