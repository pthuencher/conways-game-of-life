class GameContext:

    def __init__(self, opts):
        self.opts = opts

        if "size" in opts:
            try:
                size = opts["size"].split("x")
                self.width, self.height = (int(size[0]), int(size[1]))
            except ValueError:
                print("Error: invalid size format (%r) expected (e.g. '50x50')" % opts["size"])
                exit(-1)
        else:
            self.width, self.height = 50, 50

        if "zoom" in opts:
            try:
                self.zoom = int(opts["zoom"])
            except ValueError:
                print("Error: invalid zoom format (%r) expected (e.g. 8)" % opts["zoom"])
                exit(-1)
        else:
            self.zoom = 10

        if "sleep" in opts:
            try:
                self.sleep = int(opts["sleep"])
            except ValueError:
                print("Error: invalid sleep format (%r) expected (e.g. 200 (ms))" % opts["sleep"])
                exit(-1)
        else:
            self.sleep = 200 # ms