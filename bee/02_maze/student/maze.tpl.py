'''
This file is a bit messed up because it tests Python code generated from code also tested in javascript equivalent.
Try to forget the basic Python syntax for a while.
'''


class BadPathException(Exception):
    pass

class IsNotAFlowerException(Exception):
    pass

class IsNotHoneyException(Exception):
    pass

class EmptyFlowerException(Exception):
    pass

class EmptyHoneyException(Exception):
    pass

MAP = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 1, 2, 1, 1, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

MAP_CELLS = [{
            'x': 4,
            'y': 4,
            'res': 'redFlower',
            'value': 2
        },
        {
            'x': 5,
            'y': 4,
            'res': 'redFlower',
            'value': 2
        }
       ];

ROWS = len(MAP)
COLS = len(MAP[0])

UNSET = "UNSET"
SUCCESS = "SUCCESS"
FAILURE = "FAILURE"
TIMEOUT = "TIMEOUT"
ERROR = "ERROR"

RESULT_TYPE = {
    UNSET: 0,
    SUCCESS: 1,
    FAILURE: -1,
    TIMEOUT: 2,
    ERROR: -2
}

RESULT = RESULT_TYPE[UNSET]

WALL = "WALL"
OPEN = "OPEN"
START = "START"
FINISH = "FINISH"
OBSTACLE = "OBSTACLE"

SQUARE_TYPE = {
  WALL: 0,
  OPEN: 1,
  START: 2,
  FINISH: 3,
  OBSTACLE: 4
}

PLAYER_POSITION = {
    'x': None,
    'y': None
}

FINISH_POSITION = {
    'x': None,
    'y': None
}

for y in range(ROWS):
    for x in range(COLS):
        if MAP[y][x] == SQUARE_TYPE[START]:
            PLAYER_POSITION['x'] = x
            PLAYER_POSITION['y'] = y
        if MAP[y][x] == SQUARE_TYPE[FINISH]:
            FINISH_POSITION['x'] = x
            FINISH_POSITION['y'] = y

EAST = "east"
SOUTH = "south"
WEST = "west"
NORTH = "north"

DIRECTION_TYPE = {
    NORTH: 0,
    EAST: 1,
    SOUTH: 2,
    WEST: 3
}

MOVE_POSITION = {
    DIRECTION_TYPE[EAST]: {
        'x': 1,
        'y': 0
    },
    DIRECTION_TYPE[SOUTH]: {
        'x': 0,
        'y': 1
    },
    DIRECTION_TYPE[WEST]: {
        'x': -1,
        'y': 0
    },
    DIRECTION_TYPE[NORTH]: {
        'x': 0,
        'y': -1
    }
}

PLAYER_ORIENTATION = DIRECTION_TYPE[EAST]


def student_code():
@   @code@@


def constrain_direction4(direction):
    d = direction % 4
    if d < 0:
        d += 4
    return d


def isPath(direction):
    global PLAYER_POSITION, PLAYER_ORIENTATION, MOVE_POSITION, SQUARE_TYPE, WALL, ROWS, COLS, DIRECTION_TYPE
    effective_direction = constrain_direction4(PLAYER_ORIENTATION + direction)
    test_x = PLAYER_POSITION['x'] + MOVE_POSITION[effective_direction]['x']
    test_y = PLAYER_POSITION['y'] + MOVE_POSITION[effective_direction]['y']
    if test_x < 0 or test_x >= COLS:
        return False
    elif test_y < 0 or test_y >= ROWS:
        return False
    else:
        return not MAP[test_y][test_x] == SQUARE_TYPE[WALL] and not MAP[test_y][test_x] == SQUARE_TYPE[OBSTACLE]


def isPathForward():
    return isPath(0)


def isPathRight():
    return isPath(1)


def isPathBackward():
    return isPath(2)


def isPathLeft():
    return isPath(3)


def moveForward():
    global PLAYER_POSITION, PLAYER_ORIENTATION, MOVE_POSITION
    if isPathForward():
        PLAYER_POSITION['x'] = PLAYER_POSITION['x'] + MOVE_POSITION[PLAYER_ORIENTATION]['x']
        PLAYER_POSITION['y'] = PLAYER_POSITION['y'] + MOVE_POSITION[PLAYER_ORIENTATION]['y']
    else:
        raise BadPathException()

def moveBackward():
    global PLAYER_POSITION, PLAYER_ORIENTATION, MOVE_POSITION
    if isPathBackward():
        PLAYER_POSITION['x'] = PLAYER_POSITION['x'] - MOVE_POSITION[PLAYER_ORIENTATION]['x']
        PLAYER_POSITION['y'] = PLAYER_POSITION['y'] - MOVE_POSITION[PLAYER_ORIENTATION]['y']
    else:
        raise BadPathException()

def turnLeft():
    global PLAYER_ORIENTATION
    PLAYER_ORIENTATION = {DIRECTION_TYPE[EAST]: DIRECTION_TYPE[NORTH],
                          DIRECTION_TYPE[SOUTH]: DIRECTION_TYPE[EAST],
                          DIRECTION_TYPE[WEST]: DIRECTION_TYPE[SOUTH],
                          DIRECTION_TYPE[NORTH]: DIRECTION_TYPE[WEST]
                          }[PLAYER_ORIENTATION]


def turnRight():
    global PLAYER_ORIENTATION
    PLAYER_ORIENTATION = {DIRECTION_TYPE[EAST]: DIRECTION_TYPE[SOUTH],
                          DIRECTION_TYPE[SOUTH]: DIRECTION_TYPE[WEST],
                          DIRECTION_TYPE[WEST]: DIRECTION_TYPE[NORTH],
                          DIRECTION_TYPE[NORTH]: DIRECTION_TYPE[EAST]
                          }[PLAYER_ORIENTATION]


def isDone():
    if 0 == sum([cell['remainingValue'] for cell in MAP_CELLS]):
        return True
    else:
        return False


def notDone():
    return not isDone()

def getNectar():
    x = PLAYER_POSITION['x']
    y = PLAYER_POSITION['y']
    cell = None

    isFlower = False
    for i in range(0, len(MAP_CELLS)):
        cell = MAP_CELLS[i]
        if cell['x'] == x and cell['y'] == y and cell['res'] != 'honey':
            isFlower = True
            break

    if not isFlower:
        raise IsNotAFlowerException()

    if cell['remainingValue'] <= 0:
        raise EmptyFlowerException()

    cell['remainingValue'] -= 1

def get2Nectar():
    getNectar()
    getNectar()

def makeHoney():
    x = PLAYER_POSITION['x']
    y = PLAYER_POSITION['y']
    cell = None

    isHoney = False
    for i in range(0, len(MAP_CELLS)):
        cell = MAP_CELLS[i]
        if (cell['x'] == x and cell['y'] == y and cell['res'] == 'honey'):
            isHoney = True
            break

    if not isHoney:
        raise IsNotHoneyException()

    if cell['remainingValue'] <= 0:
        raise EmptyHoneyException()

    cell['remainingValue'] -= 1

try:
    for cell in MAP_CELLS:
        cell['remainingValue'] = cell['value']
    student_code()
    if isDone():
        print("True", end='', flush=True)
    else:
        print("Pour terminer l'exercice, il faut que vous ayez accumulé toutes les ressources.", end='', flush=True)
except BadPathException:
    print("Le personnage emprunte un chemin inexistant.")
except IsNotAFlowerException:
    print("Votre personnage essaie de récolter du nectar sur un endroit qui n'est pas une fleur.")
except EmptyFlowerException:
    print("Votre personnage essaie de récolter du nectar sur une fleur qui n'a plus de nectar.")
except IsNotHoneyException:
    print("Votre personnage essaie de fabriquer du miel sur un endroit qui n'est pas une ruche.")
except EmptyHoneyException:
    print("Votre personnage essaie de fabriquer du miel dans une ruche qui est pleine.")
except Exception:
    print("Votre code n'a pas pu être testé correctement. Il y a un problème avec vos blocs !")
