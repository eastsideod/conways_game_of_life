# encoding: utf-8
import os

from io import StringIO
from absl import logging


class FileConfigure:
    def __init__(self):
        self.width = None
        self.height = None
        self.initial_cell_count = 0
        self.cells = []

    def __repr__(self):
        def to_string_from_cells(cells):
            buf = StringIO()
            buf.write('[\n')
            for cell in cells:
                buf.write('width={0}, height={1}'.format(cell[0], cell[1]))
                buf.write('\n')
            buf.write(']')
            return buf.getvalue()

        return ''.join([
            'cls=', str(type(self)),
            ', width=', str(self.width),
            ', height=', str(self.height),
            ', initial_cell_count=', str(self.initial_cell_count),
            ', cells=', to_string_from_cells(self.cells)])


def read_conf_file(file_path, out_file_conf):
    try:
        with open(file_path) as f:
            read_conf_file_impl(f, out_file_conf)
    except Exception as e:
        logging.error('Failed to load file. error={0}'.format(e))


def read_conf_file_impl(f, out_file_conf):
    parser_functor_size = len(PARSER_FUNCTORS) - 1
    readed_line_count = 0

    while True:
        line = f.readline()
        logging.debug('readed line={0}'.format(line))
        if not line:
            logging.debug('read all line.')
            return True

        parser_idx = 0
        if parser_functor_size < readed_line_count:
            parser_idx = parser_functor_size
        else:
            parser_idx = readed_line_count

        # 설정이 끝난 뒤 라인은 읽을 필요가 없다.
        if (out_file_conf.cells and
           len(out_file_conf.cells) == out_file_conf.initial_cell_count):
            return True

        PARSER_FUNCTORS[parser_idx](line, out_file_conf)
        readed_line_count += 1


def read_board_size_conf(line, out_file_conf):
    assert line
    lines = line.split(' ')
    width = int(lines[0])
    height = int(lines[1])
    assert width > 0
    assert height > 0
    out_file_conf.width = width
    out_file_conf.height = height


def read_initial_cell_count_conf(line, out_file_conf):
    assert line
    initial_cell_count = int(line)
    assert initial_cell_count > 0
    out_file_conf.initial_cell_count = initial_cell_count


def read_initial_cell_conf(line, out_file_conf):
    assert line
    assert out_file_conf.initial_cell_count > 0

    # 초기 값 이후 설정은 무시한다.
    if len(out_file_conf.cells) == out_file_conf.initial_cell_count:
        return

    lines = line.split(' ')
    width = int(lines[1])
    height = int(lines[0])
    assert width > 0
    assert height > 0
    out_file_conf.cells.append((width, height))


PARSER_FUNCTORS = [
    read_board_size_conf,
    read_initial_cell_count_conf,
    read_initial_cell_conf
]
