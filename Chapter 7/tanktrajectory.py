import math
import pygame

WIDTH=800
HEIGHT=600

SKY_COLOR = (165, 182, 209)
SHELL_COLOR = (255,255,255)
shell_start_position = (50,500)
left_gun_angle = 50
left_gun_power = 60

shell_positions = []

def draw_shell (position):
    (xpos, ypos) = position
    # Create rectangle of the shell
    shell_rect = Rect((xpos,ypos),(5,5))
    pygame.draw.ellipse(screen.surface, SHELL_COLOR, shell_rect)

def draw():
    screen.fill(SKY_COLOR)
    for this_position in shell_positions:
        draw_shell(this_position)

def update_shell_position (left_right):
    global shell_power, shell_angle, shell_start_position, shell_current_position, shell_time

    init_velocity_y = shell_power * math.sin(shell_angle)

    # Direction - multiply by -1 for left to right
    if (left_right == 'left'):
        init_velocity_x = shell_power * math.cos(shell_angle)
    else:
        init_velocity_x = shell_power * math.cos(math.pi - shell_angle)

    # Gravity constant is 9.8 m/s^2 but this is in terms of screen so instead use a suitable value
    GRAVITY_CONSTANT = 0.004
    # Constant to give a sensible distance on x axis
    DISTANCE_CONSTANT = 1.5

    # time is calculated in update cycles
    shell_x = shell_start_position[0] + init_velocity_x * shell_time * DISTANCE_CONSTANT
    shell_y = shell_start_position[1] + -1 * ((init_velocity_y * shell_time) -
        (0.5 * GRAVITY_CONSTANT * shell_time * shell_time))

    shell_current_position = (shell_x, shell_y)
    shell_time += 1


def setup_trajectory():
    global shell_positions, shell_current_position, shell_power, shell_angle, shell_time

    shell_current_position = shell_start_position

    shell_angle = math.radians (left_gun_angle)
    shell_power = left_gun_power / 40
    shell_time = 0

    while (shell_current_position[0] < WIDTH and shell_current_position[1] < HEIGHT):
        update_shell_position("left")
        shell_positions.append(shell_current_position)


setup_trajectory()