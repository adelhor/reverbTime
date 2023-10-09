from reverbTime import *
import numpy as np
from DB import *

type_of_space = input('Write the type of space that you wish to calculate the reverberation time. \n')

volume = float(input('What is the volume of space? \n'))

total_absorption = [0] * 6

while True:
    user_option = int(input("Press 1 if you want add surface to your space. Press 2 if you finish adding surfaces and want to calculate the reverberation time \n" 
                            "Press 3 if you want to add the metarial's absorption coefficient to database and press 4 if you want to see database of coefficients \n"))
    
    if user_option == 1:

        material = input('Write the material of the first surface \n')
        area = float(input('What is the size of surface? \n'))
        absorption = Space.absorption(area, material)
        total_absorption = np.add(absorption, total_absorption)

    elif user_option == 2:
        Space.calculation(volume, total_absorption)
        print('The reverberation time has been calculated')
        break

    elif user_option == 3:
        material_name = input('Write the name of the material that you want to add \n')
        Hz125 = float(input('Write the absorption coefficent for 125 Hz \n'))
        Hz250 = float(input('Write the absorption coefficent for 250 Hz \n'))
        Hz500 = float(input('Write the absorption coefficent for 500 Hz \n'))
        Hz1000 = float(input('Write the absorption coefficent for 1000 Hz \n'))
        Hz2000 = float(input('Write the absorption coefficent for 2000 Hz \n'))
        Hz4000 = float(input('Write the absorption coefficent for 4000 Hz \n'))
        DB.write_material(material_name, Hz125, Hz250, Hz500, Hz1000, Hz2000, Hz4000)

    elif user_option == 4:
        DB.show_db()
    
    else:
        break
