class Cell:

    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.alive = False
        self.opacity = 0x0

    def __repr__(self):
        return "[%d/%d]" % (self.x, self.y)
    
    def _set(self, alive):
        self.alive = alive

    def die(self):
        self._set(False)
        self.opacity = 0x30

    def awake(self):
        self._set(True)
        self.opacity = 0xff

    def toggle(self):
        self.die() if self.alive else self.awake()

    def update_opacity(self):
        if self.opacity > 0:
            self.opacity -= 1

    def color(self):
        if self.opacity > 0:
            cc = "ffffff"
            r = int(int(cc[0:2], 16) * (self.opacity / 0xff))
            g = int(int(cc[2:4], 16) * (self.opacity / 0xff))
            b = int(int(cc[4:6], 16) * (self.opacity / 0xff))
            return "#%02x%02x%02x" % (r,g,b)
        else:
            return "black"
        

