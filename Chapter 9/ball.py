class Ball():
    show = True
    
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
        
        
    def draw(self, screen):
        if (self.show == True):
            screen.draw.filled_circle(self.position, self.radius, self.color) 