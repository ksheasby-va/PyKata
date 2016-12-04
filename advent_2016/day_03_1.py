def is_valid_triangle(sides):
    for side in sides:
        if (sum(sides) - side) <= side:
            return False

    return True


def count_triangles(sides):
    triangles_list = sides.splitlines()
    count = 0
    for triangle in triangles_list:
        if is_valid_triangle([int(n) for n in triangle.split()]):
            count += 1

    return count