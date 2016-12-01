def calculate_distance(movements):
    angle = 0
    moves_made = {
        0: 0,
        90: 0,
        180: 0,
        270: 0,
    }
    for move in movements:
        if move.startswith('R'):
            angle += 90
        elif move.startswith('L'):
            angle -= 90

        if angle == 360:
            angle = 0
        if angle < 0:
            angle += 360

        distance = int(move[1:])

        moves_made[angle] += distance

    north_south_movement = moves_made[0] - moves_made[180]
    east_west_movement = moves_made[90] - moves_made[270]

    return abs(east_west_movement) + abs(north_south_movement)
