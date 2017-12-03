from functools import partial
from math import ceil, sqrt

north = lambda y, x: (y - 1, x)
south = lambda y, x: (y + 1, x)
east = lambda y, x: (y, x + 1)
west = lambda y, x: (y, x - 1)

directions = lambda y, x: (east(y, x), north(y, x), west(y, x), south(y, x))
distance_to_center = lambda cent, curr: sqrt((curr[0] - cent[0])**2 + (curr[1] - cent[1])**2)

def find_center(length):
    adjust = 1 if length % 2 == 0 else 0
    return (length / 2 - adjust), (length / 2 - adjust)

def valid_coord(grid, coord):
    try:
        return grid[coord[0]][coord[1]] is None
    except:
        return False

def build_spiral(number):
    i = int(ceil(sqrt(number)))
    spiral = [[None for _ in range(i)] for _ in range(i)]
    center = find_center(len(spiral[0]))
    current_position = center
    distance = partial(distance_to_center, center)

    for i in range(1, number + 1):
        y, x = current_position
        spiral[y][x] = i
        empty_spots = [c for c in directions(y, x) if valid_coord(spiral, c)]
        if i != number:
            current_position = sorted(empty_spots, key=distance)[0]

    return y, x, center

def calculate_distance(number):
    y, x, center = build_spiral(number)
    return abs(y - center[0]) + abs(x - center[1])


if __name__ == '__main__':
    print calculate_distance(277678)
