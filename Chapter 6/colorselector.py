WIDTH = 800
HEIGHT = 600

color_red = 0
color_green = 0
color_blue = 0

change_amount = 5

RECT_RED = Rect((40,40),(180,45))
RECT_GREEN = Rect((40,120),(180,45))
RECT_BLUE = Rect((40,200),(180,45))

button_minus_red = Actor("button_minus_red", (260,63))
button_plus_red = Actor("button_plus_red", (310,63))
button_minus_green = Actor("button_minus_green", (260,143))
button_plus_green = Actor("button_plus_green", (310,143))
button_minus_blue = Actor("button_minus_blue", (260,223))
button_plus_blue = Actor("button_plus_blue", (310,223))

def draw() :
    screen.fill((color_red, color_green, color_blue))
    
    screen.draw.filled_rect (RECT_RED, "white")
    screen.draw.filled_rect (RECT_GREEN, "white")
    screen.draw.filled_rect (RECT_BLUE, "white")
    
    screen.draw.text("Red", (45,45), fontsize=40, color="red")
    screen.draw.text(str(color_red), (160,45), fontsize=40, color="red")
    screen.draw.text("Green", (45,125), fontsize=40, color="green")
    screen.draw.text(str(color_green), (160,125), fontsize=40, color="green")
    screen.draw.text("Blue", (45,205), fontsize=40, color="blue")
    screen.draw.text(str(color_blue), (160,205), fontsize=40, color="blue")    
    
    button_minus_red.draw()
    button_plus_red.draw()
    button_minus_green.draw()
    button_plus_green.draw()
    button_minus_blue.draw()
    button_plus_blue.draw()


def update() :
    pass
    
def on_mouse_down(pos, button):
    global color_red, color_green, color_blue
    if (button == mouse.LEFT):
        if (button_minus_red.collidepoint(pos)):
            color_red -= change_amount
            if (color_red < 1):
                color_red = 0
        elif (button_plus_red.collidepoint(pos)):
            color_red += change_amount
            if (color_red > 255):
                color_red = 255
        elif (button_minus_green.collidepoint(pos)):
            color_green -= change_amount
            if (color_green < 1):
                color_green = 0
        elif (button_plus_green.collidepoint(pos)):
            color_green += change_amount
            if (color_green > 255):
                color_green = 255
        elif (button_minus_blue.collidepoint(pos)):
            color_blue -= change_amount
            if (color_blue < 1):
                color_blue = 0
        elif (button_plus_blue.collidepoint(pos)):
            color_blue += change_amount
            if (color_blue > 255):
                color_blue = 255