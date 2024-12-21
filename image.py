import tkinter

def initialize_image():
    global img_bg, img, width, height
    img_bg = [
        tkinter.PhotoImage(file="image_penpen/chip00.png"),
        tkinter.PhotoImage(file="image_penpen/chip01.png"),
        tkinter.PhotoImage(file="image_penpen/chip02.png"),
        tkinter.PhotoImage(file="image_penpen/chip03.png")
    ]

    img = img_bg[0]
    width = img.width()
    height = img.height()