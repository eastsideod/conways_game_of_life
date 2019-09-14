# conways_game_of_life

## conway`s game of life impl in python.

```
================================================
                    O
                   OOO
                  OO OO
                   OOO
                    O
================================================
```


### requirement

- ubuntu 16.04
- python 3.x


### dependencies

- absl-py (pip3 install absl-py)


### how to run(using dockerfile)

```
$ git clone https://github.com/eastsideod/conways_game_of_life
$ cd conways_game_of_life
$ docker build -t cgol:0.0 .
$ docker run -it --name cgol cgol:0.0
```


### how to run(manually)

```
$ git clone https://github.com/eastsideod/conways_game_of_life
$ python3 -m conways_game_of_life
```


## command line arguments

### ordered arguments

```
[0] - conf file name.
[1] - dump generation count.

# run conways game of life.
# load conf file 'conffile.txt'
# and dump 10 generation state.
$ python3 -m conways_game_of_life conffile.txt 10
```

### named arguments

```
v=2 (run debug mode)
conf_file (config file name)
dump_generation_count (dump generation count)
dump_file (dump file name)

# set static board size.
board_width (board width)
board_height (board height)

# set board size randomly.
board_min_width (board min width)
board_max_width (board max width)
board_min_height (board min height)
board_max_height (board max height)
```

