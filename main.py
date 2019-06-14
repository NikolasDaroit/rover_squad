# -*- coding: utf-8 -*-

from itertools import islice
from plateau import Plateau
from rover import Rover

if __name__ == '__main__':

    filename = 'test_input.txt'

    with open(filename, 'r') as file:
        # remove blank lines
        lines_gen = iter([line for line in file if line.strip()])
        # get upper right coordinates
        upper_right = tuple(map(int, next(lines_gen).strip().split(' ')))
        rover_list = []
        # create Rovers for all itens on input file and add them to rover_list
        while True:
            start_position = None
            instructions = None
            try:
                pos_x, pos_y,orientation = next(lines_gen).strip().split(' ')
                start_position = ( int(pos_x), int(pos_y), orientation)
                instructions = next(lines_gen)
                rover_list.append(Rover(coord=start_position, instructions=instructions))
            except StopIteration:
                break

        # create a plateau with all rovers in input file
        plateau = Plateau(upper_right=upper_right, rovers=rover_list)
        # make rovers explore the plateau
        plateau.rover_explore()
