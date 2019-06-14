class Node(object):
 
    def __init__(self, orientation, prev, next):
        self.orientation = orientation
        self.prev = prev
        self.next = next
 
 
class Compass(object):
 
    head = None
    tail = None
 
    def append(self, orientation):
        new_node = Node(orientation, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.head.prev = self.tail
 
    def turn_left(self):
        self.head = self.head.prev

    def turn_right(self):
        self.head = self.head.next
 
    def __str__(self):
        return self.head.orientation

    def new(self, starting):
        self.append('N')
        self.append('E')
        self.append('S')
        self.append('W')

        # set starting orientation
        while str(self).lower() != starting.lower():
            self.turn_right()

        return self

class Rover:

    def __init__(self, coord=(0,0, 'E')):
        self.x, self.y, self.face = coord
        self.compass = Compass().new(self.face)

    def __repr__(self):
        return str(self.coord)
    
    @property
    def orientation(self):
        return str(self.compass).upper()
    
    def run(self):
        return True

    def turn_right(self):
        self.compass.turn_right()

    def turn_left(self):
        self.compass.turn_left()


