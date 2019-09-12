# encoding: utf-8
import os

from io import StringIO


# BOARD_VALUE_TYPES 의 value 에 대응한다.
BOARD_RENDER_TYPES = [
    ' ',  # empty
]


# console out 말고 다른 화면 출력은 현재 고려하지 않는다.
def render(board_data):
    os.system('clear')
    assert board_data
    width = len(board_data)
    height = len(board_data[0])

    for w in range(0, width):
        buf = StringIO()
        for h in range(0, height):
            buf.write(BOARD_RENDER_TYPES[board_data[w][h]])
        print(buf.getvalue())
