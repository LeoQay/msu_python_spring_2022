"""
Console Cross-Zero game
"""


class TicTac:
    __player_names = ['X', 'O']
    __all_synonyms = [['X', 'x'], ['O', 'o']]
    __cur_player = __player_names[0]
    __nobody_name = '_'
    __error_name = 'error'
    __board = ['_' for i in range(9)]
    __step_counter = 0
    __agree_lower = ['y', 'yes', 'yep', 'ok', 'da']
    __err_modes = ['low', 'high']
    __err_mode = 'low'
    __out = True
    __stop_words = ['exit', 'end', 'stop']

    def __init__(self, first_player='O', err_mode='low', out=True):
        if err_mode in self.__err_modes:
            self.__err_mode = err_mode
        else:
            assert False, 'Wrong error mode, only \'low\' or \'high\''

        if not isinstance(out, bool):
            ret = 'Wrong out type, bool expected,' + str(type(out)) + ' given'
            assert False, ret

        self.__out = out
        self.__check_sym(first_player)
        self.__cur_player = first_player.upper()
        self.__step_counter = 0
        self.clean_board()

    def start(self):
        while True:
            winner = self.__init_and_start_game()

            if winner == self.__error_name:
                self.my_print('Err has occurred, err_mode =', self.__err_mode)
            elif winner in self.__stop_words:
                self.my_print('Stopped')
                return winner
            elif winner == self.__nobody_name:
                self.my_print('Nobody win (')
            else:
                self.my_print('Winner is', winner)

            self.my_print('Do you want to repeat game? (y/[N]): ')
            answer = input()
            if answer.strip().lower() in self.__agree_lower:
                continue

            return winner

    def __init_and_start_game(self):
        try:
            self.clean_board()
            self.my_print("Choose first player ([O] or x)")
            first_player = self.name_input().upper()
            self.__cur_player = first_player
            self.__step_counter = 0
            return self.__process_game()
        except AssertionError as err:
            ret = err.args[0]
            if ret in self.__stop_words:
                return ret
            self.my_print(ret)
            return self.__error_name

    def __process_game(self):
        while True:
            self.__step_counter += 1

            self.my_print('Turn of player', self.__cur_player, '(from 0 to 8)')
            pos = self.pos_input()

            self.turn(pos)
            self.show_board()
            winner = self.check_winner()
            if winner != self.__nobody_name:
                return winner
            if self.__step_counter == 9:
                break
        return self.__nobody_name

    def name_input(self):
        while True:
            self.my_print('>>>', end='')
            name = self.my_input()
            if name.strip() == '':
                return self.__cur_player
            if self.validate_name_input(name):
                return name

    def pos_input(self):
        while True:
            self.my_print('>>>', end='')
            token = self.my_input()
            if self.validate_pos_input(token):
                return int(token)

    def validate_name_input(self, name):
        try:
            self.__check_sym(name.strip())
        except AssertionError as err:
            if self.__err_mode == 'high':
                assert False, err.args[0]
            self.my_print(err.args[0], ', repeat please', sep='')
            return False
        return True

    def validate_pos_input(self, token):
        try:
            pos = int(token.strip())
            self.__check_pos(pos)
        except ValueError:
            if self.__err_mode == 'high':
                assert False, 'Bad token for int'
            self.my_print('Bad token for int, repeat please')
            return False
        except AssertionError as err:
            if self.__err_mode == 'high':
                assert False, err.args[0]
            self.my_print(err.args[0], ', repeat please', sep='')
            return False
        return True

    def turn(self, pos):
        self.__insert(pos, self.__cur_player)
        self.__next_player()

    def check_winner(self):
        """
        Returns name of winner if somebody win,
        else returns __nobody_name
        """
        if self.__check_winner_symbol(self.__player_names[0]):
            return self.__player_names[0]
        if self.__check_winner_symbol(self.__player_names[1]):
            return self.__player_names[1]
        return self.__nobody_name

    def clean_board(self):
        for i in range(9):
            self.__board[i] = self.__nobody_name

    def show_board(self):
        for i in range(3):
            self.my_print("|", end='')
            for j in range(3):
                self.my_print(self.__board[TicTac.convert(i, j)], end='')
                if j != 2:
                    self.my_print(' ', end='')
            self.my_print("|")

    def __insert(self, pos, sym):
        self.__check_pos(pos)
        self.__check_sym(sym)
        sym = str(sym).upper()
        self.__board[pos] = sym

    def __check_sym(self, sym):
        cond = False
        for i in range(2):
            cond = cond or sym in self.__all_synonyms[i]
        assert cond, 'Incorrect sym'

    def __next_player(self):
        if self.__cur_player in self.__all_synonyms[0]:
            self.__cur_player = self.__player_names[1]
        else:
            self.__cur_player = self.__player_names[0]

    def __check_pos(self, pos):
        assert 0 <= pos < 9, "Range error"
        assert self.__board[pos] == self.__nobody_name, "Already taken"

    def __check_winner_symbol(self, sym):
        self.__check_sym(sym)
        sym = str(sym).upper()

        for i in range(3):
            hor = True
            ver = True
            for j in range(3):
                hor = hor and (self.__board[TicTac.convert(i, j)] == sym)
                ver = ver and (self.__board[TicTac.convert(j, i)] == sym)
            if hor or ver:
                return True

        main = True
        sub = True
        for i in range(3):
            main = main and self.__board[TicTac.convert(i, i)] == sym
            sub = sub and self.__board[TicTac.convert(i, 2 - i)] == sym
        return main or sub

    def my_print(self, *args, **kwargs):
        if self.__out:
            print(*args, **kwargs)

    def my_input(self):
        token = input()
        if token.strip().lower() in self.__stop_words:
            assert False, token.strip().lower()
        return token

    @staticmethod
    def convert(lin, col):
        return 3 * lin + col


if __name__ == "__main__":
    game = TicTac()
    game.start()
