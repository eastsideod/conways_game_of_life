# encoding: utf-8
import time

from absl import flags
from absl import app as absl_app

from .app import board
from .app.board import Board
from .app import renderer


FLAGS = flags.FLAGS


# 게임에 필요한 설정 값 정의.
flags.DEFINE_integer('board_width', 0, 'set board width.')
flags.DEFINE_integer('board_height', 0, 'set board height.')

flags.DEFINE_integer('board_min_width', 80, 'set board min width.')
flags.DEFINE_integer('board_max_width', 160, 'set board max width.')
flags.DEFINE_integer('board_min_height', 40, 'set board min height.')
flags.DEFINE_integer('board_max_height', 80, 'set board max height.')
flags.DEFINE_string('game_file', 'game_file_name.txt',
                    'load game file(absolute path).')


# 프로그램 관련 설정 값 정의.
flags.DEFINE_bool('unittest', False, 'execute unittest')


def run_game_loop():
    while True:
        time.sleep(0.3)
        Board.tick()
        board_data = Board.get_board_data()
        renderer.render(board_data)


def main(argv):
    if FLAGS.unittest:
        raise NotImplementedError()
        return

    # TODO(inkeun): 인자 검사 관련 코드 추가.

    # random size
    if FLAGS.board_width == 0 and FLAGS.board_height == 0:
        board.init_board_size_by_randomly(FLAGS.board_min_width,
                                          FLAGS.board_max_width,
                                          FLAGS.board_min_height,
                                          FLAGS.board_max_height)
    else:
        board.init_board_size(FLAGS.board_width, FLAGS.board_height)

    # TODO(inkeun): 필요 시 gevent 를 사용하여 main thread / game loop thread 를 분할
    run_game_loop()


# absl app 초기화 및 main() 실행.
absl_app.run(main)

