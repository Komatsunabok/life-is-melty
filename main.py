import tkinter
import map
import keys
import image
import character

# DIR_UP = 0
# DIR_DOWN = 1
# DIR_LEFT = 2
# DIR_RIGHT = 3

tmr = 0
# key, koff = keys.get_key()

root = tkinter.Tk()
root.title("LIFE IS MELTY")
root.resizable(False, False)

root.bind("<KeyPress>", keys.key_down)
root.bind("<KeyRelease>", keys.key_up)

image.initialize_image()

img_wid, img_hei = image.get_image_size() 
img_bg = image.img_bg

map_data = map.map_data

def draw_screen():
    canvas.delete("SCREEN")
    for y in range(map.map_sizs_y):
        for x in range(map.map_size_x):
            canvas.create_image(x*img_wid+img_wid/2, 
                                y*img_hei+img_hei/2, 
                                image = img_bg[map_data[y][x]],
                                tag = "SCREEN")
    canvas.create_image(character.candy_x, character.candy_y,
                        image = image.img_candy[character.candy_img],
                        tag = "SCREEN")

def main():
    global tmr
    tmr = tmr + 1
    draw_screen()
    character.move(10)
    character.update(tmr)
    keys.key_update()
    root.after(100, main)

canvas = tkinter.Canvas(width=img_wid*map.map_size_x,
                        height=img_hei*map.map_sizs_y)
canvas.pack()

main()

root.mainloop()
