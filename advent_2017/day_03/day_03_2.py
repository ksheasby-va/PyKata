from functools import partial
from math import ceil, sqrt

from day_03.day_03_1 import find_center, distance_to_center, directions, valid_coord

north_east = lambda y, x: (y - 1, x + 1)
north_west = lambda y, x: (y - 1, x - 1)
south_east = lambda y, x: (y + 1, x + 1)
south_west = lambda y, x: (y + 1, x - 1)

secondary_directions = lambda y, x: (north_east(y, x), north_west(y, x), south_east(y, x), south_west(y, x))

def check_neighbours(spiral, y, x):
    adjacent_values = [spiral[v[0]][v[1]] for v in directions(y, x) if spiral[v[0]][v[1]]]
    adjacent_values += [spiral[w[0]][w[1]] for w in secondary_directions(y, x) if spiral[w[0]][w[1]]]
    return sum(adjacent_values)


def build_spiral(number):
    i = int(ceil(sqrt(number)))
    spiral = [[None for _ in range(i)] for _ in range(i)]
    center = find_center(len(spiral[0]))
    current_position = center
    distance = partial(distance_to_center, center)

    for i in range(1, number + 1):
        y, x = current_position
        sum_of_neighbours = check_neighbours(spiral, y, x)
        if sum_of_neighbours > number:
            return sum_of_neighbours
        spiral[y][x] = sum_of_neighbours if sum_of_neighbours else 1
        empty_spots = [c for c in directions(y, x) if valid_coord(spiral, c)]
        if i != number:
            current_position = sorted(empty_spots, key=distance)[0]

    return None


if __name__ == '__main__':
    print build_spiral(277678)
