# -*- coding: utf-8 -*-

class Plateau():
    def __init__(self, upper_right=(5,5), rovers=[]):
        self.upper_right = upper_right
        self.bottom_left = (0,0)
        self.rovers = rovers

    def rover_explore(self):
        for rover in self.rovers:
            if max(rover.coord) > min(self.upper_right) or min(rover.coord) < min(self.bottom_left):
                raise ValueError('Rover {} could not explore, due to start position being outsite the plateau '.format(rover))

            rover.start()
            print(rover)
