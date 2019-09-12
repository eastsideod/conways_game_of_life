# encoding: utf-8
import random


BOARD_VALUE_TYPES = {
    'empty': 0,
}


class Board:
    BOARD = None
    IS_INITIALIZED = False
    BOARD_WIDTH = 0
    BOARD_HEIGHT = 0

    @staticmethod
    def init(width, height):
        assert width > 0
        assert height > 0
        assert not Board.IS_INITIALIZED

        Board.BOARD_WIDTH = width
        Board.BOARD_HEIGHT = height
        # TODO(inkeun): 차후 numpy.array 로 교체를 고려한다.
        Board.BOARD = list()
        for w in range(0, Board.BOARD_WIDTH):
            Board.BOARD.append(list())
            for h in range(0, Board.BOARD_HEIGHT):
                Board.BOARD[w].append(list())
                Board.BOARD[w][h] = BOARD_VALUE_TYPES['empty']

        Board.IS_INITIALIZED = True

    @staticmethod
    def reset():
        raise NotImplementedError()

    @staticmethod
    def tick():
        pass

    @staticmethod
    def get_board_data():
        return Board.BOARD


def init_board_size(board_width, board_height):
    assert board_width > 0
    assert board_height > 0
    Board.init(board_width, board_height)


def init_board_size_by_randomly(board_min_width, board_max_width,
                                board_min_height, board_max_height):
    assert board_min_width > 0 and board_max_width >= board_min_width
    assert board_max_width > 0
    assert board_min_height > 0 and board_max_height >= board_min_height
    assert board_max_height > 0

    Board.init(
        random.randrange(board_min_width, board_max_width + 1),
        random.randrange(board_min_height, board_max_height + 1))
