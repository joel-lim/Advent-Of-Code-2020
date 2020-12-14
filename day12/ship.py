from abc import ABC, abstractmethod
from enum import Enum


class ShipBase(ABC):
    def read(self, instruction):
        action = instruction[0]
        val = int(instruction[1:])
        if action == 'N':
            self.move(Direction.NORTH, val)
        elif action == 'S':
            self.move(Direction.SOUTH, val)
        elif action == 'E':
            self.move(Direction.EAST, val)
        elif action == 'W':
            self.move(Direction.WEST, val)
        elif action == 'L':
            self.rotate_left(val)
        elif action == 'R':
            self.rotate_right(val)
        elif action == 'F':
            self.move_forward(val)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    @abstractmethod
    def move(self, direction, val):
        pass

    @abstractmethod
    def move_forward(self, val):
        pass

    @abstractmethod
    def rotate_right(self, direction, val):
        pass

    def rotate_left(self, degrees):
        self.rotate_right(360 - (degrees % 360))


class Ship(ShipBase):
    def __init__(self):
        self.direction = Direction.EAST
        self.x = 0
        self.y = 0

    def move(self, direction, val):
        x, y = direction.value
        self.x += x * val
        self.y += y * val

    def move_forward(self, val):
        self.move(self.direction, val)

    def rotate_right(self, degrees):
        turns = (degrees // 90) % 4
        for _ in range(turns):
            self.direction = self.direction.next()

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class ShipWithWaypoint(ShipBase):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_waypoint = 10
        self.y_waypoint = 1

    def move(self, direction, val):
        x, y = direction.value
        self.x_waypoint += x * val
        self.y_waypoint += y * val

    def move_forward(self, val):
        x_shift = (self.x_waypoint) * val
        y_shift = (self.y_waypoint) * val
        self.x += x_shift
        self.y += y_shift

    def rotate_right(self, degrees):
        turns = (degrees // 90) % 4
        for _ in range(turns):
            self.x_waypoint, self.y_waypoint = self.y_waypoint, -self.x_waypoint


class Direction(Enum):
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)
    NORTH = (0, 1)

    def next(self):
        x, y = self.value
        return Direction((y, -x))
