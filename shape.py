
class Blinker:

    def coords(self, x ,y):
        return [
            (x, y),
            (x + 1, y),
            (x + 2, y)
        ]

class Glider:

    def coords(self, x, y):
        return [
            (x, y),
            (x + 1, y),
            (x + 2, y),
            (x + 2, y - 1),
            (x + 1, y - 2)
        ]
    
