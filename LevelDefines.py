
# number of rows for
BRICK_LAYOUT_ROWS = 9
# number of columns for
BRICK_LAYOUT_COLS = 9

# level layouts for bricks
BRICK_LAYOUTS = \
    [
        # test / scheme level
        [0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         3, 3, 3, 3, 3, 1, 3, 3, 3,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0],

        # level 1
        [0, 0, 0, 0, 1, 0, 0, 0, 0,
         0, 0, 0, 1, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 1, 0, 0, 0, 0,
         0, 2, 2, 2, 2, 2, 2, 2, 0,
         0, 2, 1, 1, 1, 1, 1, 2, 0,
         0, 2, 1, 0, 0, 0, 1, 2, 0,
         0, 2, 1, 0, 0, 0, 1, 2, 0,
         0, 2, 1, 1, 1, 1, 1, 2, 0,
         0, 0, 2, 2, 2, 2, 2, 0, 0],

        # level 2
        [1, 2, 2, 2, 2, 2, 2, 2, 1,
         2, 2, 1, 0, 2, 0, 1, 2, 2,
         2, 1, 0, 1, 2, 1, 0, 1, 2,
         2, 1, 0, 1, 2, 1, 0, 1, 2,
         2, 2, 0, 0, 0, 0, 0, 2, 2,
         2, 1, 0, 3, 3, 3, 0, 1, 2,
         2, 1, 0, 0, 0, 0, 0, 1, 2,
         2, 2, 1, 1, 2, 1, 1, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 2, 1],

        # level 3
        [1, 2, 0, 0, 0, 0, 0, 2, 1,
         2, 1, 0, 0, 1, 0, 0, 1, 2,
         0, 0, 0, 1, 2, 1, 0, 0, 0,
         0, 0, 1, 2, 3, 2, 1, 0, 0,
         0, 0, 1, 2, 3, 2, 1, 0, 0,
         0, 1, 2, 3, 3, 3, 2, 1, 0,
         0, 1, 2, 3, 3, 3, 2, 1, 0,
         1, 2, 2, 2, 2, 2, 2, 2, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

LEVEL_NUM = len(BRICK_LAYOUTS)


BRICKS_PER_ROW = 9
BRICK_ROWS = 9
BRICK_SPACE = [2, 2]
# brick status
BRICK_DESTR = 0
BRICK_NORMAL = 1
BRICK_ADV = 2
BRICK_UNDESTR = 3
BRICK_SPECIAL = 4
# brick sprite image according to status
BRICK_IMAGE = \
    [
        "res/img/blank.png",
        "res/img/blue.png",
        "res/img/gold.png",
        "res/img/red.png",
        "res/img/brick_special.png"
    ]
