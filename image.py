import tkinter

img_bg = []
img_candy = []

def initialize_image():
    global img_bg, img_candy
    img_bg = [
        tkinter.PhotoImage(file="image/map/map01.png"),
        tkinter.PhotoImage(file="image/map/map02.png"),
        tkinter.PhotoImage(file="image/map/map03.png")
    ]

    img_candy = [
        tkinter.PhotoImage(file="image/character/back-stationary.png"),
        tkinter.PhotoImage(file="image/character/back-L.png"),
        tkinter.PhotoImage(file="image/character/back-R.png"),
        tkinter.PhotoImage(file="image/character/front-stationary.png"),
        tkinter.PhotoImage(file="image/character/front-L.png"),
        tkinter.PhotoImage(file="image/character/front-R.png"),
        tkinter.PhotoImage(file="image/character/left-stationary.png"),
        tkinter.PhotoImage(file="image/character/left-L.png"),
        tkinter.PhotoImage(file="image/character/left-R.png"),
        tkinter.PhotoImage(file="image/character/right-stationary.png"),
        tkinter.PhotoImage(file="image/character/right-L.png"),
        tkinter.PhotoImage(file="image/character/right-R.png")
    ]

def get_image_size():
    return 60, 60 #面倒なので固定値を返す