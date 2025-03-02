import tkinter
import map
import key
import image

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3


def draw_screen():
    canvas.delete("SCREEN")
    for y in range(map.map_sizs_y):
        for x in range(map.map_size_x):
            canvas.create_image(x*image.width+image.width/2, 
                                y*image.height+image.height/2, 
                                image = image.img_bg[map.map_data[y][x]],
                                tag = "SCREEN")
            canvas.create_image()

root = tkinter.Tk()
root.title("LIFE IS MELTY")
root.resizable(False, False)

image.initialize_image()

canvas = tkinter.Canvas(width=image.width*map.map_size_x,
                        height=image.height*map.map_sizs_y)
canvas.pack()




draw_screen()



root.mainloop()
