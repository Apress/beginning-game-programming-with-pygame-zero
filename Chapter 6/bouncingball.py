WIDTH = 800
HEIGHT = 600

# starting positions
ball_x = 400
ball_y = 300
ball_speed = 5
# Velocity seperated into x and y components
ball_velocity = [0.7 * ball_speed, 1 * ball_speed]
ball_radius = 20
ball_color_pos = 0

def draw():
    screen.clear()
    draw_ball()
    
def update():
    global ball_x, ball_y, ball_velocity, ball_color_pos
    ball_color_pos += 1
    if (ball_color_pos > 255):
        ball_color_pos = 0
    ball_x += (ball_velocity[0])
    ball_y += (ball_velocity[1]) 
    if (ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0): 
        ball_velocity[0] = ball_velocity[0] * -1
    if (ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0): 
        ball_velocity[1] = ball_velocity[1] * -1


def draw_ball():
    color = color_wheel (ball_color_pos)
    screen.draw.filled_circle ((ball_x,ball_y), ball_radius, color)
    
# Cycle around a colour wheel - 0 to 255
def color_wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)
        
        