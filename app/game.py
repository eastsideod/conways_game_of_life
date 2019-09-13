# encoding: utf-8
from absl import logging

from .board import (BOARD_VALUE_TYPES, BOARD_VALUES,
                    Board, Cell)


def tick():
    Board.GENERATION_COUNT += 1
    delete_cells = []
    new_cells = []
    if not calculate_cell_states(Board.get_board_data(),
                                 Board.get_cells(),
                                 new_cells, delete_cells):
        logging.error('Failed to calculate cell states.')
        return False

    logging.debug('new_cells={0}'.format(new_cells))
    logging.debug('delete_cells={0}'.format(new_cells))

    Board.commit(new_cells, delete_cells)


def is_allowed_board_data(value):
    return value in BOARD_VALUES


def get_neighbors_by_cell(board_data, cell):
    board_width = len(board_data)
    board_height = len(board_data[0])

    range_width_min = max(cell.width - 1, 0)
    range_width_max = min(cell.width + 2, board_width)

    range_height_min = max(cell.height - 1, 0)
    range_height_max = min(cell.height + 2, board_height)

    searched_board_values = []
    neighbor_cells_count = 0
    for w in range(range_width_min, range_width_max):
        for h in range(range_height_min, range_height_max):
            if w == cell.width and h == cell.height:
                continue

            if board_data[w][h] != BOARD_VALUE_TYPES['empty']:
                neighbor_cells_count += 1

            searched_board_values.append((w, h, board_data[w][h]))
    return (neighbor_cells_count, searched_board_values)


def calculate_cell_states(board_data, alive_cells,
                          out_new_cells, out_delete_cells):
    assert board_data and type(board_data) == list
    assert alive_cells and type(alive_cells) == list
    assert type(out_new_cells) == list
    assert type(out_delete_cells) == list

    nearby_empty_board_blocks = {}

    if not board_data:
        logging.error('Not found board data.')
        return False

    if not alive_cells:
        logging.error('No cell are alive.')
        return False

    for cell in alive_cells:
        (neighbor_cnt, search_result) = get_neighbors_by_cell(board_data, cell)
        # 인접 세포 카운트가 2, 3 이 아닌 경우 죽는다.
        if neighbor_cnt not in (2, 3):
            out_delete_cells.append(cell)

        # 새로운 세포 생성을 위해 탐색된 주변 8칸에 대해서 중첩 탐색 된 값을 쌓는다.
        for r in search_result:
            assert len(r) == 3
            width = r[0]
            height = r[1]
            value = r[2]
            assert width >= 0
            assert height >= 0
            assert is_allowed_board_data(value)

            if value == BOARD_VALUE_TYPES['empty']:
                position = (width, height)
                if position not in nearby_empty_board_blocks:
                    nearby_empty_board_blocks[position] = 1
                else:
                    nearby_empty_board_blocks[position] += 1

    logging.debug('calculated nearby_empty_board_blocks={0}'.format(
        nearby_empty_board_blocks))

    for position, cnt in nearby_empty_board_blocks.items():
        if cnt == 3:
            out_new_cells.append(
                Cell(position[0], position[1]))

    return True

