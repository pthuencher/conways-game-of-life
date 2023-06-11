class Cell:

    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.alive = False
        self.changed = True

    def __repr__(self):
        return "[%d/%d]" % (self.x, self.y)
    
    def _set(self, alive):
        self.alive = alive
        self.changed = True # render

    def die(self):
        self._set(False)

    def awake(self):
        self._set(True)

    def toggle(self):
        self._set(not self.alive)
