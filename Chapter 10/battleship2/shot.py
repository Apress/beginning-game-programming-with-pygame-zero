from pgzero.actor import Actor

class Shot(Actor):

    def __init__ (self, hit, pos):
        Actor.__init__(self,hit)
        self.topleft=pos