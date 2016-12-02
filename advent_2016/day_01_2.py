def add_location_to_list(locations, location_x, location_y):
    location_found = False
    if (location_x, location_y) in locations:
        location_found = True

    locations.append((location_x, location_y))

    return locations, location_found


def calculate_positions(movements):
    angle = 0
    locations = [(0, 0)]
    location_found = False
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

        for i in xrange(distance):

            if len(locations) == 0:
                location_x = 0
                location_y = 0
            else:
                location_x = locations[-1][0]
                location_y = locations[-1][1]

            location_x += {90: 1,
                           270: -1,
                           }.get(angle, 0)
            location_y += {0: 1,
                           180: -1,
                           }.get(angle, 0)

            locations, location_found = add_location_to_list(locations, location_x, location_y)
            if location_found:
                break
        if location_found:
            break

    return locations
