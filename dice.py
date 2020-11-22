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


    return dice


print(dice_get_command('2d4'))