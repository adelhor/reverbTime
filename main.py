from reverbTime import *
#import matplotlib.pyplot as plt
import numpy as np

type_of_space = input('Write the type of space \n')

volume = float(input('What is the volume of space? \n'))

total_absorption = [0] * 6

while True:
    user_option = int(input("Press 1 if you want add surface to your space. Press 2 if you finish adding surfaces and want to calculate the reverberation time \n"))
    
    if user_option == 1:

        material = input('Write the material of the first surface \n')
        area = float(input('What is the size of surface? \n'))
        absorption = Space.absorption(area, material)
        total_absorption = np.add(absorption, total_absorption)

    elif user_option == 2:
        Space.calculation(volume, total_absorption)
        print('The reverberation time has been calculated')
        break

    else:
        break
