import copy


def add_square_to_grid(coords, grid):
    coord_pieces = [int(c) for c in coords.split()[2].replace(":", "").split(",")]
    sizes = [int(c) for c in coords.split()[3].split("x")]
    for i in range(sizes[0]):
        for j in range(sizes[1]):
            if grid[coord_pieces[1] + j][coord_pieces[0] + i] == "#":
                grid[coord_pieces[1] + j][coord_pieces[0] + i] = "X"
            else:
                grid[coord_pieces[1] + j][coord_pieces[0] + i] = "#"
    return grid


def make_grid(input, size):
    line = ["."] * size
    grid = []
    for i in range(size):
        grid.append(copy.deepcopy(line))
    for i in input.splitlines():
        grid = add_square_to_grid(i, grid)
    print len(grid)
    print grid
    return grid


if __name__ == "__main__":
    make_grid("#1 @ 0,1: 3x1", 4)