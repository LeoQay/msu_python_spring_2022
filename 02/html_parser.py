class HtmlParser:
    def __init__(self,
                 open_tag_callback,
                 data_callback,
                 close_tag_callback):
        self.token_stack = []
        self.stack = []
        self.html_str = ''
        self.pos = 0
        self.open_call = open_tag_callback
        self.data_call = data_callback
        self.close_call = close_tag_callback

    def __del__(self):
        self.clear()

    def clear(self) -> None:
        self.stack.clear()
        self.token_stack.clear()
        self.html_str = ''
        self.pos = 0

    def start(self, html_str: str) -> None:
        self.clear()
        self.html_str = html_str.strip()
        self.make_token_stack()
        self.process_token_stack()

    def process_token_stack(self) -> None:
        for token in self.token_stack:
            self.push(token)

    def push(self, token: (str, str)) -> None:
        if token[1] == 'data':
            self.push_data(token[0])
        elif token[1] == 'open':
            self.push_open(token[0])
        elif token[1] == 'close':
            self.push_close(token[0])
        else:
            answer = 'Wrong token type: ' + token[1] + ' of ' + token[0]
            raise ValueError(answer)

    def push_data(self, data_token: str) -> None:
        if len(self.stack) == 0:
            raise SyntaxError('Missing open tag')
        self.stack[-1][1].append(data_token)

    def push_open(self, open_tag: str) -> None:
        self.stack.append((open_tag, [], ''))

    def push_close(self, close_tag: str) -> None:
        if len(self.stack) == 0:
            raise SyntaxError('Missing open tag')
        if not HtmlParser.is_tag_pair(self.stack[-1][0], close_tag):
            answer = 'Tags doesn\'t make pair: '
            answer += '\'' + self.stack[-1][0] + '\''
            answer += ' and '
            answer += '\'' + close_tag + '\''
            raise SyntaxError(answer)
        last = self.stack[-1]
        self.run_tag_calls((last[0], last[1], close_tag))
        del self.stack[-1]

    @staticmethod
    def is_tag_pair(open_tag: str, close_tag: str) -> bool:
        return open_tag[1:-1].lower() == close_tag[2:-1].lower()

    def make_token_stack(self) -> None:
        if self.html_str.strip() == '':
            return

        # append first tag
        self.token_stack.append(self.get_tag_token())

        while self.pos < len(self.html_str):
            data_start = self.pos
            tag_token = self.get_next_tag_token()
            if tag_token is None:
                raise SyntaxError('Missing tag')
            data_end = self.html_str.rfind('<', data_start + 1, self.pos)
            data = self.html_str[data_start:data_end]
            self.token_stack.append((data, 'data'))
            self.token_stack.append(tag_token)

    def get_next_tag_token(self) -> (str, str) or None:
        save_self_pos = self.pos
        while True:
            self.pos = self.html_str.find('<', self.pos)
            if self.pos == -1:
                self.pos = save_self_pos
                return None
            try:
                return self.get_tag_token()
            except SyntaxError:
                pass
            self.pos += 1

    def get_tag_token(self) -> (str, str):
        if self.html_str[self.pos] != '<':
            raise SyntaxError('It is not tag token')

        pos = self.html_str.find('>', self.pos + 1)
        if pos == -1:
            raise SyntaxError('Missing close \'>\' in tag')

        tag_token = self.html_str[self.pos:pos + 1]

        if not HtmlParser.is_tag_token(tag_token):
            raise SyntaxError('Wrong tag token')

        self.pos = pos + 1

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

        return tag_token[left:-1].strip().isalpha()

    def run_tag_calls(self, tag_info: (str, list, str)) -> None:
        self.open_call(tag_info[0])
        self.data_call(''.join(tag_info[1]))
        self.close_call(tag_info[2])


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
