# key
key = ""
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global key
    key = ""

def key_update():
    global key, koff
    if koff == True:
        key = ""
        koff = False


def get_key():
    return key, koff

# def set_key(k, koff_):
#     global key, koff
#     key = k
#     koff = koff_