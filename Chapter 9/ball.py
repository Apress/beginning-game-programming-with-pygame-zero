class Ball():
    shape = "Sphere"
    
    def __init__(self, position, radius, color):
        self.position = position
        self.radius = radius
        self.color = color
        
        
    def draw(self, screen):
        screen.draw.filled_circle(self.position, self.radius, self.color) 
