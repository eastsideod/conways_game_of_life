# encoding: utf-8
import time

from absl import flags, logging
from absl import app as absl_app

from .app import board, game, renderer
from .app.board import Board, Cell
from .app.file_args_parser import read_conf_file, FileConfigure


FLAGS = flags.FLAGS


# 게임에 필요한 설정 값 정의.
flags.DEFINE_integer('board_width', 0, 'set board width.')
flags.DEFINE_integer('board_height', 0, 'set board height.')

flags.DEFINE_integer('board_min_width', 80, 'set board min width.')
flags.DEFINE_integer('board_max_width', 90, 'set board max width.')
flags.DEFINE_integer('board_min_height', 40, 'set board min height.')
flags.DEFINE_integer('board_max_height', 50, 'set board max height.')
flags.DEFINE_string('conf_file', '', 'load game file(absolute path).')


# 프로그램 관련 설정 값 정의.
flags.DEFINE_bool('unittest', False, 'execute unittest')


def run_game_loop():
    while True:
        time.sleep(5)
        print('================================================')
        print('generation - {0}'.format(Board.GENERATION_COUNT))
        board_data = Board.get_board_data()
        renderer.render(board_data)
        if Board.is_cell_all_dead():
            print('all cell are dead.')
            print('================================================')
            exit(0)
            return

        game.tick()
        print('================================================')


def main(argv):
    if FLAGS.unittest:
        raise NotImplementedError()
        return

    file_conf = None
    initial_cell_conf = []

    if FLAGS.conf_file:
        file_conf = FileConfigure()
        logging.info('read configure from file. file={0}'.format(
            FLAGS.conf_file))

        read_conf_file(FLAGS.conf_file, file_conf)
        logging.debug('file_conf={0}'.format(file_conf))

        assert file_conf.width > 0
        assert file_conf.height > 0
        assert file_conf.cells

        FLAGS.board_width = file_conf.width
        FLAGS.board_height = file_conf.height
        initial_cell_conf = file_conf.cells

    # TODO(inkeun): 인자 검사 관련 코드 추가.

    # random size
    if FLAGS.board_width == 0 and FLAGS.board_height == 0:
        board.init_board_size_by_randomly(FLAGS.board_min_width,
                                          FLAGS.board_max_width,
                                          FLAGS.board_min_height,
                                          FLAGS.board_max_height)
        logging.debug('The board size was initialized randomly. ',
                      'board_min_width=', FLAGS.board_min_width,
                      'board_max_width=', FLAGS.board_max_width,
                      'board_min_height=', FLAGS.board_min_height,
                      'board_max_height=', FLAGS.board_max_height)
    else:
        board.init_board_size(FLAGS.board_width, FLAGS.board_height)
        logging.debug('The board size was initialized specific size. ')
        logging.debug('board_width={0}'.format(FLAGS.board_width))
        logging.debug('board_height={0}'.format(FLAGS.board_height))

    for cell_conf in initial_cell_conf:
        Board.append_cell(Cell(cell_conf[0], cell_conf[1]))

    # TODO(inkeun): 필요 시 gevent 를 사용하여 main thread / game loop thread 를 분할
    run_game_loop()


# absl app 초기화 및 main() 실행.
absl_app.run(main)
