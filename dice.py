from random import randint


def dice_get_command(str_command):
    # return dice=[x,y,'operation',z] or False
    dice = []

    d_command = str_command.upper()
    if 'D' not in d_command:
        return False

    # geting X
    l_command = d_command.split('D')
    if l_command[0] == '':
        dice.append(1)
    else:
        dice.append(int(l_command[0]))

    # geting Y,Z
    if '+' in l_command[1]:
        z = l_command[1].split('+')
        dice += [int(z[0]), '+', int(z[1])]
    elif '-' in l_command[1]:
        z = l_command[1].split('-')
        dice += [int(z[0]), '-', int(z[1])]
    else:
        dice.append(int(l_command[1]))

    # dice type
    print(dice)
    if not dice[1] in [3, 4, 6, 8, 10, 12, 20, 100]:
        print(f'Nie znam kostki {dice[1]}-ściennej!')
        return False

    return dice


print(dice_get_command('2d4'))