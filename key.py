# key
key = ""
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True