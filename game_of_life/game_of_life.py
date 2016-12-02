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
    height = len(grid) / width
    neighbours = []
    top_row = list_index < width
    bottom_row = ((position + 1) / (width + 1)) == height
    left_side = (position % width) == 1
    right_side = (position % width) == 0
    if not top_row and not left_side:
        neighbours.append(grid[list_index - width - 1])
    if not top_row:
        neighbours.append(grid[list_index - width])
    if not top_row and not right_side:
        neighbours.append(grid[list_index - width + 1])
    if not left_side:
        neighbours.append(grid[list_index - 1])
    if not left_side and not bottom_row:
        neighbours.append(grid[list_index + width - 1])
    if not right_side:
        neighbours.append(grid[list_index + 1])
    if not bottom_row:
        neighbours.append(grid[list_index + width])
    if not bottom_row and not right_side:
        neighbours.append(grid[list_index + width + 1])

    return neighbours
