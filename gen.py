from cell import Cell

class Generation:

    def __init__(self, ctx, n=0):
        self.ctx = ctx
        self.n = n
        self.grid = [[Cell(x, y) for x in range(ctx.width)] for y in range(ctx.height)]

    def __repr__(self):
        width = self.ctx.width
        height = self.ctx.height

        repr = "Generation #%d\n" % self.n
        repr += " -" * width + "\n"
        for y in range(height):
            for x in range(width):
                cell = self.at(x, y)
                repr += " #" if cell.alive else "  "
            repr += "\n"
        repr += " -" * width
        return repr

    def __eq__(self, other):
        equal = True
        for cell in self.iter():
            if cell.alive != other.at(cell.x, cell.y).alive:
                equal = False
                break

        return equal
    
    def iter(self):
        for y in range(self.ctx.height):
            for x in range(self.ctx.width):
                yield self.at(x, y)

    def at(self, x, y):
        return self.grid[y % self.ctx.height][x % self.ctx.width]
    
    def count_alive_neighbors(self, cell):
        x = cell.x
        y = cell.y
        count = 0

        for xn,yn in [
            (x-1,y-1),(x,y-1),(x+1,y-1),    # * * *
            (x-1,y),(x+1,y),                # * X *
            (x-1,y+1),(x,y+1),(x+1,y+1)     # * * *
        ]:
            if self.at(xn, yn).alive:
                count += 1

        return count
