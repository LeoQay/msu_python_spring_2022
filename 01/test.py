import unittest
import tic_tac as tt


class TicTacTest(unittest.TestCase):
    game = tt.TicTac(out=False)
    turn_counter = 0

    def do_test_turn(self, pos, winner):
        self.game.turn(pos)
        self.turn_counter += 1
        self.assertEqual(self.game.check_winner(), winner)

    def do_test_game(self, first_player, game_list, winner):
        self.game = tt.TicTac(first_player, err_mode='high', out=False)
        self.turn_counter = 0

        for i in range(len(game_list) - 1):
            self.do_test_turn(game_list[i], '_')

        self.do_test_turn(game_list[-1], winner.upper())


class TicTacTestFewGames(TicTacTest):
    def test_just_game_1(self):
        self.do_test_game('X', [0, 1, 2, 3, 4, 5, 6], 'X')

    def test_just_game_2(self):
        self.do_test_game('o', [0, 8, 1, 7, 2], 'o')

    def test_just_game_3(self):
        self.do_test_game('X', [4, 2, 0, 8, 5, 3, 7, 1, 6], '_')

    def test_just_game_4(self):
        self.do_test_game('X', [4, 2, 0, 8, 5, 3, 7, 1, 6], '_')

    def test_just_game_5(self):
        self.do_test_game('X', [0, 2, 4, 6, 8], 'X')


class TicTacTestDraws(TicTacTest):
    def test_draw_case_1(self):
        self.do_test_game('X', [0, 1, 2, 4, 3, 6, 5, 8, 7], '_')

    def test_draw_case_2(self):
        self.do_test_game('O', [6, 2, 7, 4, 0, 8, 1, 3, 5], '_')

    def test_draw_case_3(self):
        self.do_test_game('X', [0, 1, 2, 4, 3, 6, 5, 8, 7], '_')


class TicTacTestWinnerGames(TicTacTest):
    """
    Testing all winner cases:
    3 vertical, 3 horizon, 2 diagonal.
    """

    def test_winner_case_horizon_up_1(self):
        self.do_test_game('X', [0, 3, 1, 4, 2], 'X')

    def test_winner_case_horizon_up_2(self):
        self.do_test_game('O', [5, 0, 7, 1, 8, 2], 'X')

    def test_winner_case_horizon_mid_1(self):
        self.do_test_game('X', [3, 0, 4, 1, 5], 'X')

    def test_winner_case_horizon_mid_2(self):
        self.do_test_game('O', [0, 3, 8, 4, 2, 5], 'X')

    def test_winner_case_horizon_down_1(self):
        self.do_test_game('O', [6, 0, 7, 1, 8], 'O')

    def test_winner_case_horizon_down_2(self):
        self.do_test_game('X', [0, 6, 1, 7, 5, 8], 'O')

    def test_winner_case_vertical_left_1(self):
        self.do_test_game('O', [0, 2, 3, 4, 6], 'O')

    def test_winner_case_vertical_left_2(self):
        self.do_test_game('X', [8, 0, 7, 6, 2, 3], 'O')

    def test_winner_case_vertical_mid_1(self):
        self.do_test_game('X', [1, 8, 4, 6, 7], 'X')

    def test_winner_case_vertical_mid_2(self):
        self.do_test_game('O', [3, 1, 5, 4, 0, 7], 'X')

    def test_winner_case_vertical_right_1(self):
        self.do_test_game('X', [2, 0, 5, 1, 8], 'X')

    def test_winner_case_vertical_right_2(self):
        self.do_test_game('O', [1, 2, 4, 5, 0, 8], 'X')

    def test_winner_case_diag_main_1(self):
        self.do_test_game('X', [0, 3, 4, 5, 8], 'X')

    def test_winner_case_diag_main_2(self):
        self.do_test_game('O', [3, 8, 7, 4, 2, 0], 'X')

    def test_winner_case_diag_sub_1(self):
        self.do_test_game('X', [2, 0, 4, 1, 6], 'X')

    def test_winner_case_diag_sub_2(self):
        self.do_test_game('O', [5, 4, 0, 6, 8, 2], 'X')


class TicTacTestValidateName(TicTacTest):
    """ Testing name validator """

    def __do_name_validate_test(self, name, ret):
        self.game = tt.TicTac(out=False)
        self.assertEqual(ret, self.game.validate_name_input(name))

    def test_validate_name_1(self):
        self.__do_name_validate_test('X', True)

    def test_validate_name_2(self):
        self.__do_name_validate_test('x', True)

    def test_validate_name_3(self):
        self.__do_name_validate_test('O', True)

    def test_validate_name_4(self):
        self.__do_name_validate_test('o', True)

    def test_validate_name_5(self):
        self.__do_name_validate_test('  X   ', True)

    def test_validate_name_6(self):
        self.__do_name_validate_test('    o    ', True)

    def test_validate_name_7(self):
        self.__do_name_validate_test('Xx', False)

    def test_validate_name_8(self):
        self.__do_name_validate_test('xo', False)

    def test_validate_name_9(self):
        self.__do_name_validate_test('2134', False)

    def test_validate_name_10(self):
        self.__do_name_validate_test('Name  ', False)

    def test_validate_name_11(self):
        self.__do_name_validate_test('', False)

    def test_validate_name_12(self):
        self.__do_name_validate_test('  ', False)


class TicTacTestPosValidator(TicTacTest):
    """ Testing position validator """

    def __do_pos_validate_test(self, token, ret):
        self.game = tt.TicTac(out=False)
        self.assertEqual(ret, self.game.validate_pos_input(token))

    def test_validate_pos_1(self):
        """All good values"""
        for i in range(9):
            self.__do_pos_validate_test(str(i), True)

    def test_validate_pos_2(self):
        """Other good values"""
        for i in range(9):
            self.__do_pos_validate_test('  ' + str(i) + '   ', True)

    def test_validate_pos_3(self):
        self.__do_pos_validate_test('X', False)

    def test_validate_pos_4(self):
        self.__do_pos_validate_test('o', False)

    def test_validate_pos_5(self):
        self.__do_pos_validate_test('', False)

    def test_validate_pos_6(self):
        self.__do_pos_validate_test('    ', False)

    def test_validate_pos_7(self):
        self.__do_pos_validate_test('12agr', False)

    def test_validate_pos_8(self):
        self.__do_pos_validate_test('0af', False)

    def test_validate_pos_9(self):
        self.__do_pos_validate_test('X2', False)

    def test_validate_pos_10(self):
        """Out of range testing"""
        for i in ['-1', '10', '11', '111', '21', '9', '-12']:
            self.__do_pos_validate_test(i, False)


class TicTacTestInit(TicTacTest):
    def test_init_1(self):
        try:
            self.game = tt.TicTac()
        except AssertionError:
            assert False

    def test_init_2(self):
        try:
            self.game = tt.TicTac(err_mode='low')
        except AssertionError:
            assert False

    def test_init_3(self):
        try:
            self.game = tt.TicTac(err_mode='high')
        except AssertionError:
            assert False

    def test_init_4(self):
        try:
            self.game = tt.TicTac(err_mode='invalid')
        except AssertionError:
            pass
        else:
            assert False

    def test_init_5(self):
        try:
            self.game = tt.TicTac(err_mode='')
        except AssertionError:
            pass
        else:
            assert False

    def test_init_6(self):
        try:
            self.game = tt.TicTac(out='reh')
        except AssertionError:
            pass
        else:
            assert False

    def test_init_7(self):
        try:
            self.game = tt.TicTac(out=23)
        except AssertionError:
            pass
        else:
            assert False

    def test_init_8(self):
        try:
            self.game = tt.TicTac(out=True)
        except AssertionError:
            assert False

    def test_init_9(self):
        try:
            self.game = tt.TicTac(out=False)
        except AssertionError:
            assert False


class TicTacTestRepeat(TicTacTest):
    def test_repeat_1(self):
        try:
            self.do_test_game('X', [0, 0], '_')
        except AssertionError:
            pass
        else:
            assert False

    def test_repeat_2(self):
        try:
            self.do_test_game('X', [1, 2, 7, 2], '_')
        except AssertionError:
            pass
        else:
            assert False

    def test_repeat_3(self):
        try:
            self.do_test_game('X', [0, 1, 2, 4, 3, 6, 5, 8, 4], '_')
        except AssertionError:
            pass
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
