from pgzero.actor import Actor

class Shot(Actor):

    def update(self, time_interval):
        self.y-=3 * 60 * time_interval