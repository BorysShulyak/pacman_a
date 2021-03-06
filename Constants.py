# Screen constants
ROWS = 25
COLS = 25
WIDTH, HEIGHT = COLS * 20 + 50, ROWS * 20 + 50
FPS = 60
BORDER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH - BORDER, HEIGHT - BORDER


# Colour constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (187, 187, 187)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Font constants
START_TEXT_SIZE = 36
START_FONT = 'Sans Serif'

# Game states
MENU = 1
GAMING = 2
GAME_OVER = 3
WINNER = 4

# Player constants
PLAYER_COLOUR = (255, 70, 0)
PLAYER_LIVES = 5
START = (1, 1)
DESTINATION = (ROWS - 2, COLS - 2)

All_COINS = 1
ONLY_WAY = 2

#Map constants
WALL = 1
COIN = 2
PLAYER = 3
BLOCKED = 1
EMPTY = 0
COIN_AMOUNTS = 5
