
while True:
    #get inputs
    width = input ('What is the width of the Room? ')
    length = input ('What is the length of the Room? ')
    hight = input ('What is the height of the Room? ')

    #Calculation
    area = float(width)*float(length)
    volume = float(width)*float(length)*float(hight)

    #shift unit
    area_sqmm = area * 1000000
    volume_qmm = volume * 1000000000 

    #print area and volume
    print('The room has a area of {} sqm. and a volume of {} qm.'.format(area, volume))
    print('which corresponds to {} sqmm. and a volume of {} qmm.'.format(area_sqmm, volume_qmm))

    #determine largest variable
    if width > length and width > hight:
        print('The dominant variable is the width.')

    elif length > hight and length > width:
        print('The dominant variable is the length.')

    elif length == hight and length == width:
        print('All variables are the same.')

    elif length == hight:
        print('Length and hight are the same dominant.')

    elif length == width:
        print('Length and width are the same dominant.')

    elif hight == width:
        print('Hight and width are the same dominant.')

    else:
        print('The dominant variable is the hight.')

    restart = input('Want to calculate a new Room? (yes/no): ')
    if restart.lower() != 'yes':
        break