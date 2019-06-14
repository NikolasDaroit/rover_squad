import unittest
from rover import Rover
# from plateau import Plateau
class TestRover(unittest.TestCase):
    # order (N E S W)
    def setUp(self):
        self.rover = Rover(coord=(2,2,'W'))
    
    def test_rover_compass_should_return_west(self):
        assert self.rover.orientation() == 'W'

    def test_rover_turn_right_should_return_north(self):
        self.rover.turn_right()
        assert self.rover.orientation() == 'N'

    def test_rover_turn_left_should_return_south(self):
        self.rover.turn_left()
        assert self.rover.orientation() == 'S'

    def test_rover_turn_right_360_should_return_west(self):
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        assert self.rover.orientation() == 'W'

    def test_rover_turn_left_360_should_return_west(self):
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        assert self.rover.orientation() == 'W'

    def test_rover_move_west_should_decrease_x_by_1(self):
        self.rover.move()
        assert self.rover.coord == (1,2)

    def test_rover_turn_right_move_north_should_increase_y_by_1(self):
        self.rover.turn_right()
        self.rover.move()
        assert self.rover.coord == (2,3)

    def test_rover_turn_right_move_east_should_increase_x_by_1(self):
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.move()
        assert self.rover.coord == (3,2)

    def test_rover_turn_left_move_south_should_decrease_y_by_1(self):
        self.rover.turn_left()
        self.rover.move()
        assert self.rover.coord == (2,1)


if __name__ == '__main__':
    unittest.main()
