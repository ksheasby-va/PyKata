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
