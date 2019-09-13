# encoding: utf-8
import random

from absl import logging


BOARD_VALUE_TYPES = {
    'empty': 0,
    'alive': 1,
}


BOARD_VALUES = (0, 1)


class Cell:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return ''.join(['cls=', str(type(self)),
                        ', width=', str(self.width),
                        ', height=', str(self.height)])


class Board:
    BOARD = None
    IS_INITIALIZED = False
    BOARD_WIDTH = 0
    BOARD_HEIGHT = 0
    # TODO(inkeun): (width, height), (value) dict로 변경할 것을 고려.
    CELLS = []

    GENERATION_COUNT = 0

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
    def append_cell(cell):
        assert type(cell) == Cell
        logging.debug('cell appended. ')
        logging.debug('cell={0}'.format(cell))
        Board.CELLS.append(cell)
        Board.BOARD[cell.width][cell.height] = BOARD_VALUE_TYPES['alive']

    @staticmethod
    def commit(new_cells, delete_cells):
        commit_impl(Board.BOARD, Board.CELLS, new_cells, delete_cells)

    @staticmethod
    def get_board_data():
        return Board.BOARD

    @staticmethod
    def get_cells():
        return Board.CELLS

    @staticmethod
    def is_cell_all_dead():
        return len(Board.CELLS) == 0


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


def commit_impl(board_data, alive_cells, new_cells, delete_cells):
    for cell in new_cells:
        alive_cells.append(cell)
        board_data[cell.width][cell.height] = BOARD_VALUE_TYPES['alive']

    for cell in delete_cells:
        for idx in range(0, len(alive_cells)):
            if (cell.width == alive_cells[idx].width and
               cell.height == alive_cells[idx].height):
                logging.debug('delete cell. cell={0}'.format(cell))
                alive_cells.pop(idx)
                board_data[cell.width][cell.height] = BOARD_VALUE_TYPES[
                    'empty']
                break
