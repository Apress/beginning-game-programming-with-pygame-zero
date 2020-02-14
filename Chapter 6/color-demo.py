# Program to demonstrate some of the color words including in Pygame / Pygame Zero
import pygame

WIDTH = 800
HEIGHT = 600

colors = ['aquamarine1', 'black', 'blue', 'magenta', 'gray', 'green', 'limegreen', 'maroon', 'navy',
    'brown', 'purple', 'red', 'lightgray', 'orange', 'white', 'yellow', 'violet']

def draw():
    screen.draw.filled_rect(Rect((400,0),(400,600)),(255,255,255))
    line_number = 0
    for color in colors:
        print_color (color, line_number)
        line_number += 1


def print_color (colorname, line_number):
    color_rgb_string = "{},{},{}".format(pygame.Color(colorname).r, pygame.Color(colorname).g, pygame.Color(colorname).b)
    color_html_string = "#{:02x}{:02x}{:02x}".format(pygame.Color(colorname).r, pygame.Color(colorname).g, pygame.Color(colorname).b)
    screen.draw.text(colorname, (20,30*(line_number+1)), color=colorname)
    screen.draw.text(color_rgb_string, (130,30*(line_number+1)), color=colorname)
    screen.draw.text(color_html_string, (250,30*(line_number+1)), color=colorname)
    screen.draw.text(colorname, (420,30*(line_number+1)), color=colorname)
    screen.draw.text(color_rgb_string, (530,30*(line_number+1)), color=colorname)
    screen.draw.text(color_html_string, (650,30*(line_number+1)), color=colorname)