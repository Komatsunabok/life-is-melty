import tkinter
import map
import key
import image

def draw_screen():
    for y in range(map.map_sizs_y):
        for x in range(map.map_size_x):
            canvas.create_image(x*image.width+image.width/2, 
                                y*image.height+image.height/2, 
                                image = image.img_bg[map.map_data[y][x]])

root = tkinter.Tk()
root.title("LIFE IS MELTY")
root.resizable(False, False)

image.initialize_image()

canvas = tkinter.Canvas(width=image.width*map.map_size_x,
                        height=image.height*map.map_sizs_y)
canvas.pack()




draw_screen()



root.mainloop()
