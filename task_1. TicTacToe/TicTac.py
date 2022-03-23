"""
Console Cross-Zero game
"""


def convert(i, j):
    return 3 * i + j


class TicTac:
    """Main class for Cross-Zero game"""
    __player_names = ['X', 'O']
    __all_synonyms = [['X', 'x'], ['O', 'o']]
    __current_player = __player_names[0]
    __nobody_name = '_'
    __board = ['_' for i in range(9)]

    def __init__(self, first_player='O'):
        self.__check_sym(first_player)
        self.__current_player = first_player.upper()

    def __del__(self):
        for i, it in enumerate(self.__board):
            self.__board[i] = self.__nobody_name

    def start_game(self):
        print("Choose first player >>> ", end='')
        first_player = input()
        self.__check_sym(first_player)
        first_player = first_player.upper()
        self.__current_player = first_player

        self.__process_game()

    def __process_game(self):
        """
        Main cycle of game, turn by turn of players.
        Returns winners name.
        """
        winner = self.__nobody_name
        while True:
            self.validate_input()
            self.show_board()
            winner = self.check_winner()
            if winner != self.__nobody_name:
                break
        print('Winner is', winner)
        return winner

    def validate_input(self):
        print('Turn of player', self.__current_player, end='')
        print(' (from 0 to 8) >>> ', end='')
        pos = int(input())
        self.turn(pos)

    def turn(self, pos):
        self.__insert(pos, self.__current_player)
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

    def show_board(self):
        for i in range(3):
            print("| ", end='')
            for j in range(3):
                print(self.__board[convert(i, j)], " ", sep='', end='')
            print("|")

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
        if self.__current_player in self.__all_synonyms[0]:
            self.__current_player = self.__player_names[1]
        else:
            self.__current_player = self.__player_names[0]

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
                hor = hor and (self.__board[convert(i, j)] == sym)
                ver = ver and (self.__board[convert(j, i)] == sym)
            if hor or ver:
                return True

        main = True
        sub = True
        for i in range(3):
            main = main and self.__board[convert(i, i)] == sym
            sub = sub and self.__board[convert(i, 2 - i)] == sym
        return main or sub


if __name__ == "__main__":
    game = TicTac()
    game.start_game()
