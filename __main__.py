# encoding: utf-8
from absl import flags
from absl import app as absl_app


FLAGS = flags.FLAGS


# 게임에 필요한 설정 값 정의.
flags.DEFINE_integer('board_min_width', 80, 'set board min width.')
flags.DEFINE_integer('board_max_width', 160, 'set board max width.')
flags.DEFINE_integer('board_min_height', 40, 'set board min height.')
flags.DEFINE_integer('board_max_height', 80, 'set board max height.')
flags.DEFINE_string('game_file', 'game_file_name.txt',
                    'load game file(absolute path).')


# 프로그램 관련 설정 값 정의.
flags.DEFINE_bool('unittest', False, 'execute unittest')


def main(argv):
    if FLAGS.unittest:
        raise NotImplementedError()
        return
    else:
        raise NotImplementedError()


# absl app 초기화 및 main() 실행.
absl_app.run(main)
