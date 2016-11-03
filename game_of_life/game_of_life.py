def game_of_life(width, height, grid):
    """ https://github.com/garora/TDD-Katas#game-of-life- """
    return make_grid_from_list(width, grid)


def make_grid_from_list(width, grid):
    i = 1
    string = ''
    for cell in grid:
        if (i % width) == 0:
            i = 1
            string += cell
            string += '\n'
        else:
            i += 1
            string += cell

    return string
