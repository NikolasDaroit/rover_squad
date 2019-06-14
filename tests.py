import unittest
from rover import Rover
class TestRover(unittest.TestCase):
    # order (N E S W)
    def setUp(self):
        self.rover = Rover(coord=(2,2,'W'))
        # print(self.rover.coord)
    
    def test_rover_compass_should_return_west(self):
        assert self.rover.orientation == 'W'

    def test_rover_turn_right_should_return_north(self):
        self.rover.turn_right()
        assert self.rover.orientation == 'N'

    def test_rover_turn_left_should_return_south(self):
        self.rover.turn_left()
        assert self.rover.orientation == 'S'

    def test_rover_turn_right_360_should_return_west(self):
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        self.rover.turn_right()
        assert self.rover.orientation == 'W'

    def test_rover_turn_left_360_should_return_west(self):
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        self.rover.turn_left()
        assert self.rover.orientation == 'W'

if __name__ == '__main__':
    unittest.main()
