# -*- coding: utf-8 -*-
class Rover:

    def __init__(self, coord=(0,0, 'E'), instructions=None):
        self.x, self.y, self.face = coord
        self.compass = Compass().new(self.face)
        self._instructions = instructions

    def __repr__(self):
        '''
        show rover in a expected output format
        '''
        return '{} {} {}'.format(self.x, self.y, self.compass)

    def _show_info(self):
        '''
        shows info from current rover state
        '''
        return 'Rover: coords = ({}, {}) facing = {} instructions = {}'.format(self.x, self.y, self.compass, self.instructions)

    @property
    def instructions(self):
        '''
        separate instruction string in a list
        '''
        return list(self._instructions.strip())

    @property
    def coord(self):
        '''
        return rover current coordinates 
        '''
        return (self.x, self.y)

    def orientation(self):
        '''
        return which direction the rover is facing 
        '''
        return str(self.compass).upper()
    
    def move(self):
        '''
        move the rover based on its facing direction
        '''
        if self.orientation() == 'W':
            self.x -= 1
        elif self.orientation() == 'E':
            self.x += 1
        elif self.orientation() == 'S':
            self.y -= 1
        elif self.orientation() == 'N':
            self.y += 1

    def start(self):
        '''
        execute all instructions from the rover
        M - move 
        L - turn left 
        R - turn right 
        '''
        for instruction in self.instructions:
            if instruction == 'M':
                self.move()
            elif instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()

    def turn_right(self):
        '''
        turn right the rover facing direction 
        '''
        self.compass.turn_right()

    def turn_left(self):
        ''' 
        turn right the rover facing direction 
        '''
        self.compass.turn_left()


class Node:
 
    def __init__(self, orientation, prev, next):
        self.orientation = orientation
        self.prev = prev
        self.next = next
 
 
class Compass:
    '''
    Compass acts like the orientation tool for the rover.
    It indicates the rover orientation.
    Doubly Linked List
    '''
 
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

    def new(self, starting):
        self.append('N')
        self.append('E')
        self.append('S')
        self.append('W')

        # set starting orientation
        while str(self).lower() != starting.lower():
            self.turn_right()

        return self

    def __repr__(self):
        return self.head.orientation
