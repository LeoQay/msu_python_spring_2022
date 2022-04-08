import os
import filecmp
import unittest
import factory
from unittest.mock import patch
import html_parser as hp


class HardTestHtmlParser(unittest.TestCase):
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

    def do_test_input_output(self, test_name: str):
        self.set_test_name(test_name)
        html_str = self.get_input_str()
        self.parse_to_file(html_str)
        is_equal = filecmp.cmp(self.test_file_name, self.validator_name)
        self.assertTrue(is_equal)


class JustFewTestHtmlParser(HardTestHtmlParser):
    def test_io_simple(self):
        self.do_test_input_output('simple')

    def test_io_1(self):
        self.do_test_input_output('io1')

    def test_io_2(self):
        self.do_test_input_output('io2')


class SimpleTestHtmlParser(HardTestHtmlParser):
    def test_io_3(self):
        """ Empty file """
        self.do_test_input_output('io3')

    def test_io_4(self):
        """ One empty tag """
        self.do_test_input_output('io4')

    def test_io_5(self):
        """ Two empty tags """
        self.do_test_input_output('io5')

    def test_io_6(self):
        """ One tag and some data """
        self.do_test_input_output('io6')

    def test_io_7(self):
        """ Little recursion """
        self.do_test_input_output('io7')


class TestParserCalls(unittest.TestCase):
    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_empty(self,
                   do_open_call_mock,
                   do_data_call_mock,
                   do_close_call_mock):
        hp.parse_html("")

        self.assertEqual(do_open_call_mock.call_count, 0)
        self.assertEqual(do_data_call_mock.call_count, 0)
        self.assertEqual(do_close_call_mock.call_count, 0)

    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_simple_calls(self,
                          do_open_call_mock,
                          do_data_call_mock,
                          do_close_call_mock):
        hp.parse_html("<html></html>")

        self.assertEqual(do_open_call_mock.call_count, 1)
        self.assertEqual(do_open_call_mock.call_args[0][0], '<html>')

        self.assertEqual(do_data_call_mock.call_count, 1)
        self.assertEqual(do_data_call_mock.call_args[0][0], '')

        self.assertEqual(do_close_call_mock.call_count, 1)
        self.assertEqual(do_close_call_mock.call_args[0][0], '</html>')

    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_one_data(self,
                      do_open_call_mock,
                      do_data_call_mock,
                      do_close_call_mock):
        hp.parse_html("<title>Some data</title>")

        self.assertEqual(do_open_call_mock.call_count, 1)
        self.assertEqual(do_open_call_mock.call_args[0][0], '<title>')

        self.assertEqual(do_data_call_mock.call_count, 1)
        self.assertEqual(do_data_call_mock.call_args[0][0], 'Some data')

        self.assertEqual(do_close_call_mock.call_count, 1)
        self.assertEqual(do_close_call_mock.call_args[0][0], '</title>')

    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_some_data(self,
                       do_open_call_mock,
                       do_data_call_mock,
                       do_close_call_mock):
        hp.parse_html("<html>data1<body>data2</body>data3</html>")

        self.assertEqual(do_open_call_mock.call_count, 2)
        self.assertEqual(do_open_call_mock.call_args[0][0], '<body>')

        self.assertEqual(do_data_call_mock.call_count, 2)
        self.assertEqual(do_data_call_mock.call_args[0][0], 'data1data3')

        self.assertEqual(do_close_call_mock.call_count, 2)
        self.assertEqual(do_close_call_mock.call_args[0][0], '</html>')

    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_some_not_call_data(self,
                                do_open_call_mock,
                                do_data_call_mock,
                                do_close_call_mock):
        inp = "data1<html>data2</html>data3"
        hp.parse_html(inp)

        self.assertEqual(do_open_call_mock.call_count, 1)
        self.assertEqual(do_open_call_mock.call_args[0][0], '<html>')

        self.assertEqual(do_data_call_mock.call_count, 1)
        self.assertEqual(do_data_call_mock.call_args[0][0], 'data2')

        self.assertEqual(do_close_call_mock.call_count, 1)
        self.assertEqual(do_close_call_mock.call_args[0][0], '</html>')


class TestWrongInputHtmlParser(unittest.TestCase):
    def test_wrong_pair_tag(self):
        inp = '<html>Something</body>'
        self.assertRaises((SyntaxError,), hp.parse_html, inp)

    def test_missing_close_tag(self):
        inp = '<title>data data data'
        self.assertRaises((SyntaxError,), hp.parse_html, inp)

    def test_missing_open_tag(self):
        inp = 'data data data</title>'
        self.assertRaises((SyntaxError,), hp.parse_html, inp)


class TestDifficultHtmlParser(unittest.TestCase):
    @patch('html_parser.HtmlParser.do_close_call')
    @patch('html_parser.HtmlParser.do_data_call')
    @patch('html_parser.HtmlParser.do_open_call')
    def test_difficult_symbols(self,
                               do_open_call_mock,
                               do_data_call_mock,
                               do_close_call_mock):
        inp = '<title>data ><data    d<ata</title>'
        hp.parse_html(inp)

        self.assertEqual(do_open_call_mock.call_count, 1)
        self.assertEqual(do_open_call_mock.call_args[0][0], '<title>')

        self.assertEqual(do_data_call_mock.call_count, 1)
        self.assertEqual(do_data_call_mock.call_args[0][0],
                         'data ><data    d<ata')

        self.assertEqual(do_close_call_mock.call_count, 1)
        self.assertEqual(do_close_call_mock.call_args[0][0], '</title>')


if __name__ == '__main__':
    unittest.main()
