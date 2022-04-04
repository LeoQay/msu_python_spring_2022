class HtmlParser:
    def __init__(self,
                 open_tag_callback,
                 data_callback,
                 close_tag_callback):
        self.token_stack = []
        self.token_stack_ptr = 0
        self.stack = []
        self.html_str = ['', 0]
        self.open_call = open_tag_callback
        self.data_call = data_callback
        self.close_call = close_tag_callback

    def __del__(self):
        self.clear()

    def clear(self) -> None:
        self.stack.clear()
        self.token_stack.clear()
        self.token_stack_ptr = 0
        self.html_str = ['', 0]

    def start(self, html_str: str) -> None:
        self.clear()
        self.html_str = [html_str.strip(), 0]
        self.make_token_stack()
        self.stack = self.get_tags()
        if self.token_stack_ptr != len(self.token_stack):
            raise SyntaxError('Syntax error')
        self.run_tags(self.stack)

    def run_tags(self, tag_list):
        for tag in tag_list:
            self.run_tag(tag)

    def run_tag(self, tag):
        self.open_call(tag[0])
        self.run_tags(tag[1])
        self.data_call(''.join(tag[2]))
        self.close_call(tag[3])

    def get_tags(self):
        ret = []
        while True:
            tag = self.get_tag()
            if tag is None:
                return ret
            ret.append(tag)

    def get_tag(self) -> ():
        open_tag = self.get_token()
        if open_tag is None:
            return None
        if open_tag[1] != 'open':
            self.return_token()
            return None
        data_list = []
        tag_list = []
        while True:
            token = self.get_token()
            if token is None:
                raise SyntaxError('Close tag lost')
            if token[1] == 'data':
                data_list.append(token[0])
            elif token[1] == 'open':
                self.return_token()
                tag_list.append(self.get_tag())
            elif token[1] == 'close':
                return open_tag[0], tag_list, data_list, token[0]

    @staticmethod
    def is_tag_pair(open_tag: str, close_tag: str) -> bool:
        return open_tag[1:-1].lower() == close_tag[2:-1].lower()

    def return_token(self):
        if self.token_stack_ptr <= 0:
            raise IndexError('Token stack index out range')
        self.token_stack_ptr -= 1

    def get_token(self):
        if self.token_stack_ptr >= len(self.token_stack):
            return None
        ret = self.token_stack[self.token_stack_ptr]
        self.token_stack_ptr += 1
        return ret

    def make_token_stack(self) -> None:
        if self.html_str[0].strip() == '':
            return

        # append first tag
        self.token_stack.append(self.get_tag_token())

        while self.html_str[1] < len(self.html_str[0]):
            data_start = self.html_str[1]
            tag_token = self.get_next_tag_token()
            if tag_token is None:
                raise SyntaxError('Missing tag')
            data_end = \
                self.html_str[0].rfind('<', data_start + 1, self.html_str[1])
            data = self.html_str[0][data_start:data_end]
            self.token_stack.append((data, 'data'))
            self.token_stack.append(tag_token)

    def get_next_tag_token(self) -> (str, str) or None:
        save_self_pos = self.html_str[1]
        while True:
            self.html_str[1] = self.html_str[0].find('<', self.html_str[1])
            if self.html_str[1] == -1:
                self.html_str[1] = save_self_pos
                return None
            try:
                return self.get_tag_token()
            except SyntaxError:
                pass
            self.html_str[1] += 1

    def get_tag_token(self) -> (str, str):
        if self.html_str[0][self.html_str[1]] != '<':
            raise SyntaxError('It is not tag token')

        pos = self.html_str[0].find('>', self.html_str[1] + 1)
        if pos == -1:
            raise SyntaxError('Missing close \'>\' in tag')

        tag_token = self.html_str[0][self.html_str[1]:pos + 1]

        if not HtmlParser.is_tag_token(tag_token):
            raise SyntaxError('Wrong tag token')

        self.html_str[1] = pos + 1

        if tag_token[1] == '/':
            return ''.join(['</', tag_token[2:-1].strip(), '>']), 'close'

        return ''.join(['<', tag_token[1:-1].strip(), '>']), 'open'

    @staticmethod
    def is_tag_token(tag_token: str) -> bool:
        if len(tag_token) <= 2:
            return False

        left = 1
        if tag_token[left] == '/':
            left = 2

        if tag_token[left].isspace():
            return False

        tag_token = tag_token[left:-1].strip()

        if len(tag_token) == 0 or tag_token[0] == '-':
            return False

        for sym in tag_token:
            if not (sym.isalpha() or sym.isdigit() or sym in '_-'):
                return False
        return True


def parse_html(html_str: str,
               open_tag_callback,
               data_callback,
               close_tag_callback):
    parser = HtmlParser(open_tag_callback,
                        data_callback,
                        close_tag_callback)
    parser.start(html_str)


def print_open_tag(tok: str):
    print("Open tag:", tok)


def print_close_tag(tok: str):
    print("Close tag:", tok)


def print_data(tok: str):
    print("Data:", tok)


if __name__ == "__main__":
    with open("for_test.html", "r", encoding='UTF-8') as file:
        parse_html(''.join(file), print_open_tag, print_data, print_close_tag)
