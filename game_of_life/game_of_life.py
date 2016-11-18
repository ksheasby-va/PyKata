def game_of_life(width, height, grid):
    """ https://github.com/garora/TDD-Katas#game-of-life- """
    return make_grid_from_list(width, grid)


def make_grid_from_list(width, grid):
    """
    Return the string representation of the grid, with proper line breaks.
    width: integer of width of the grid.
    grid: list 1-D representation of the grid
    """
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


def get_neighbours(position, width, grid):
    list_index = position - 1
    neighbours = []
    if position > width:
        neighbours.append(grid[list_index - width - 1])
        neighbours.append(grid[list_index - width])
        neighbours.append(grid[list_index - width + 1])
        neighbours.append(grid[list_index - 1])
        neighbours.append(grid[list_index + width - 1])
    neighbours.append(grid[list_index + 1])
    neighbours.append(grid[list_index + width])
    neighbours.append(grid[list_index + width + 1])

    return neighbours
