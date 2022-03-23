import unittest
import TicTac as Tt


class TicTacTest(unittest.TestCase):
    game = Tt.TicTac()
    turn_counter = 0
    test_lib = []

    def run_game_tests(self):
        for it in self.test_lib:
            self.__do_game_test(*it)

    def __do_turn(self, pos, winner):
        self.game.turn(pos)
        self.turn_counter += 1
        self.assertEqual(self.game.check_winner(), winner)

    def __do_game(self, first_player, game_list, winner):
        self.game = Tt.TicTac(first_player)
        self.turn_counter = 0

        for i in range(len(game_list) - 1):
            self.__do_turn(game_list[i], '_')

        self.__do_turn(game_list[-1], winner.upper())

    def __do_game_test(self, test_num, first_player, game_list, winner):
        try:
            self.__do_game(first_player, game_list, winner)
        except AssertionError:
            print("Test", test_num, "failed on", self.turn_counter, "turn")
        else:
            print("Test", test_num, "passed")

    def make_tests(self):
        self.test_lib.append((1, 'X', [0, 1, 2, 3, 4, 5, 6], 'X'))
        self.test_lib.append((2, 'o', [0, 8, 1, 7, 2], 'o'))
        self.test_lib.append((3, 'X', [4, 2, 0, 8, 5, 3, 7, 1, 6], '_'))
        self.test_lib.append((4, 'X', [4, 2, 0, 8, 5, 3, 7, 1, 6], '_'))
        self.test_lib.append((5, 'X', [0, 2, 4, 6, 8], 'X'))


if __name__ == "__main__":
    test = TicTacTest()
    test.make_tests()
    test.run_game_tests()
