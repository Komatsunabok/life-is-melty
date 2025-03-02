import tkinter

def initialize_image():
    global img_bg, img, width, height
    img_bg = [
        tkinter.PhotoImage(file="image/map/map01.png"),
        tkinter.PhotoImage(file="image/map/map02.png"),
        tkinter.PhotoImage(file="image/map/map03.png")
    ]

    img = img_bg[0]
    width = img.width()
    height = img.height()