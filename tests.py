# -*- coding: utf-8 -*-

import unittest
import io
import sys
from rover import Rover
from plateau import Plateau

class TestRover(unittest.TestCase):

    # order (N E S W)
    def setUp(self):

        self.rover = Rover(coord=(2,2,'W'))
        self.rover1 = Rover(coord=(1,2,'N'), instructions='LMLMLMLMM')
        self.rover2 = Rover(coord=(3,3,'E'), instructions='MMRMMRMRRM')
        self.expected_output_rover1 = '1 3 N'
        self.expected_output_rover2 = '5 1 E'
        self.expected_output = '{}\n{}\n'.format(self.expected_output_rover1, self.expected_output_rover2)
    
    def test_rover_compass_should_return_west(self):
        self.assertEqual(self.rover.orientation(), 'W')

    def test_rover_turn_right_should_return_north(self):
        self.rover.turn_right()
        self.assertEqual(self.rover.orientation(), 'N')

    def test_rover_turn_left_should_return_south(self):
        self.rover.turn_left()
        self.assertEqual(self.rover.orientation(), 'S')

    def test_rover_turn_right_360_should_return_west(self):
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        self.assertEqual(self.rover.orientation(), 'W')

    def test_rover_turn_left_360_should_return_west(self):
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        self.assertEqual(self.rover.orientation(), 'W')

    def test_rover_move_west_should_decrease_x_by_1(self):
        self.rover.move()
        self.assertEqual(self.rover.coord, (1,2))

    def test_rover_turn_right_move_north_should_increase_y_by_1(self):
        self.rover.turn_right()
        self.rover.move()
        self.assertEqual(self.rover.coord, (2,3))

    def test_rover_turn_right_move_east_should_increase_x_by_1(self):
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.move()
        self.assertEqual(self.rover.coord, (3,2))

    def test_rover_turn_left_move_south_should_decrease_y_by_1(self):
        self.rover.turn_left()
        self.rover.move()
        self.assertEqual(self.rover.coord, (2,1))

    def test_rover_position_greater_than_plateau_should_raise_exception(self):
        rover = Rover(coord=(4,0,'E'))
        plateau = Plateau(upper_right=(3,3), rovers=[rover])
        self.assertRaises(ValueError, plateau.rover_explore)

        rover = Rover(coord=(3, -1,'E'))
        plateau = Plateau(upper_right=(3,3), rovers=[rover])
        self.assertRaises(ValueError, plateau.rover_explore)

    def test_plateau_rover_explore_should_print_expected_output(self):
        plateau = Plateau(upper_right=(3,3), rovers=[self.rover1, self.rover2])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        plateau.rover_explore()
        sys.stdout = sys.__stdout__
        output = capturedOutput.getvalue()
        
        self.assertEqual(output, self.expected_output)
        
    def test_rover_execute_instruction_should_return_1_3_N(self):
        self.rover1.start()
        self.assertEqual(str(self.rover1), self.expected_output_rover1)
        

    def test_rover_execute_instruction_should_return_5_1_E(self):
        self.rover2.start()
        self.assertEqual(str(self.rover2), self.expected_output_rover2)

if __name__ == '__main__':
    unittest.main()
