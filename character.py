import image
import map
import keys

img_wid = image.get_image_size()[0]
map_data = map.map_data

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3

ANIMATION = [0, 1, 0, 2]

candy_x = 90
candy_y = 90
candy_dir = 0
candy_img = 0

def isWall(cx, cy, dir, dot):
    iswall = False
    if dir == DIR_UP:
        map_x = int((cx-img_wid/2)/img_wid)
        map_y = int((cy-img_wid/2-dot)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True      
        map_x = int((cx+img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
    if dir == DIR_DOWN:
        map_x = int((cx-img_wid/2)/img_wid)
        map_y = int((cy+img_wid/2+dot)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
        map_x = int((cx+img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
    if dir == DIR_LEFT:
        map_x = int((cx-img_wid/2-dot)/img_wid)
        map_y = int((cy-img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
        map_y = int((cy+img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
    if dir == DIR_RIGHT:
        map_x = int((cx+img_wid/2+dot)/img_wid)
        map_y = int((cy-img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
        map_y = int((cy+img_wid/2)/img_wid)
        if map_data[map_y][map_x] <= 1:
            iswall = True
    return iswall

def move(dot):
    key = keys.get_key()[0]
    global candy_x, candy_y, candy_dir, candy_img
    if key == 'Up':
        candy_dir = DIR_UP
        if not isWall(candy_x, candy_y, DIR_UP, dot):
            candy_y -= dot
    if key == 'Down':
        candy_dir = DIR_DOWN
        if not isWall(candy_x, candy_y, DIR_DOWN, dot):
            candy_y += dot
    if key == 'Left':
        candy_dir = DIR_LEFT
        if not isWall(candy_x, candy_y, DIR_LEFT, dot):
            candy_x -= dot
    if key == 'Right':
        candy_dir = DIR_RIGHT
        if not isWall(candy_x, candy_y, DIR_RIGHT, dot):
            candy_x += dot

def update(tmr):
    global candy_img
    if keys.get_key()[0] == "":
        candy_img = candy_dir*3
    else:
        candy_img = candy_dir*3 + ANIMATION[tmr%4]