import tkinter as tk

from copy import deepcopy
from functools import partial
from sys import exit

from ctx import GameContext
from gen import Generation
from shape import *



class ConwaysGameOfLife(tk.Tk):

    def __init__(self, opts):
        super().__init__()
        self.title("Conway's Game of Life")
        self.ctx = GameContext(opts)
        self.gen = Generation(self.ctx)
        self.last_gen = None
        self.running = False

    def loop(self):

        if self.running:

            self.evolve()
            self.render()
            # restart loop
            self.after(self.ctx.sleep, self.loop)

    def on_space(self, event):
        self.running = not self.running
        if self.running:
            self.after(0, self.loop)

    def on_click_cell(self, cell, event):
        cell.toggle()
        self.render()

    def launch(self):
        self.tkinit()
        # start game loop
        self.after(0, self.loop)
        # start tkinter loop
        self.mainloop()

    def tkinit(self):

        self.bind("<space>", self.on_space)

        zoom = self.ctx.zoom
        self.canvas = tk.Canvas(self, width=self.ctx.width * zoom, height=self.ctx.height * zoom)
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        for cell in self.gen.iter():
            x = cell.x * zoom
            y = cell.y * zoom
            tag = "cell_%d_%d" % (cell.x, cell.y)
            
            cell.rect = self.canvas.create_rectangle(
                (x, y), 
                (x + zoom, y + zoom), 
                fill="white" if cell.alive else "black", 
                outline="black",
                tags=(tag))
            
            self.canvas.tag_bind(tag, "<Button-1>", partial(self.on_click_cell, cell))

        self.render()

    def render(self):
        for cell in self.gen.iter():
            self.canvas.itemconfigure(cell.rect, fill=cell.color()) 

    def evolve(self):
        self.last_gen = deepcopy(self.gen)
        self.gen.n = self.last_gen.n + 1

        for cell in self.last_gen.iter():

            alive_neighbors = self.last_gen.count_alive_neighbors(cell)
            new_cell = self.gen.at(cell.x, cell.y)

            if cell.alive:
                if alive_neighbors < 2:
                    new_cell.die() # under population
                elif alive_neighbors > 3:
                    new_cell.die() # over population
            else:
                if alive_neighbors == 3:
                    new_cell.awake() # reproduction
                else:
                    new_cell.update_opacity() # slowly fade away

        
        return self.last_gen != self.gen

    def add_shape(self, x, y, shape):
        for xp, yp in shape().coords(x, y):
            self.gen.at(xp, yp).awake()



if __name__ == "__main__":

    game = ConwaysGameOfLife({
        "size": "50x50",
        "zoom": 10,
        "sleep": 1
    })

    game.add_shape(5, 5, Glider)
    game.add_shape(5, 15, Glider)
    game.add_shape(5, 25, Glider)
    game.add_shape(25, 25, Blinker)

    game.launch()