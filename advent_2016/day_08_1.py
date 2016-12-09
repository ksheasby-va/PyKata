from copy import copy


def identify_command_type(command):
    if 'rect' in command:
        return 'rect'
    elif 'rotate column' in command:
        return 'rotx'
    elif 'rotate row' in command:
        return 'roty'


def execute_rect_command(screen, command):
    x = int(command.split()[1].split('x')[0])
    y = int(command.split()[1].split('x')[1])

    for i in xrange(y):
        for j in xrange(x):
            screen[i][j] = '#'
    return screen


def execute_roty_command(screen, command):
    y = int(command.split('=')[-1].split()[0])
    x = int(command.split('=')[-1].split()[-1])

    rotated_part = screen[y][-x:]
    screen[y][x:] = screen[y][0:len(screen[y]) - x]
    screen[y][0:x] = rotated_part

    return screen


def execute_rotx_command(screen, command):
    transposed = zip(*screen)
    x = int(command.split('=')[-1].split()[0])
    y = int(command.split('=')[-1].split()[-1])

    for i in xrange(len(screen[0])):
        if i == x:
            rotated_part = list(transposed[i])[-y:]
            trans_screen = list(transposed[i])
            trans_screen[y:] = list(transposed[i])[0:len(transposed[i]) - y]
            trans_screen[0:y] = rotated_part

    return_screen = list(transposed)
    return_screen[x] = trans_screen
    almost_final_screen = []
    for item in return_screen:
        if isinstance(item, tuple):
            almost_final_screen.append(list(item))
        else:
            almost_final_screen.append(item)

    final_screen = []
    for item in list(zip(*almost_final_screen)):
        final_screen.append(list(item))

    return final_screen


def count_octothorps_in_screen(screen):
    count = 0
    for item in screen:
        for pixel in item:
            if pixel == '#':
                count += 1

    return count


def count_pixels(screen, commands):
    for command in commands.splitlines():
        if identify_command_type(command) == 'rect':
            screen = execute_rect_command(screen, command)
        elif identify_command_type(command) == 'rotx':
            screen = execute_rotx_command(screen, command)
        else:
            screen = execute_roty_command(screen, command)

    return count_octothorps_in_screen(screen)
