from reverbTime import *
import numpy as np
from DB import *


while True:
    user_option = int(input("Press 1 if you want calculate the reverberation time \n"
                            "Press 2 if you want to see database of coefficients \n"
                            "Press 3 if you want to add the surfaces to the database. \n"
                            "Press 4 if you finish calculations and you want to close the console. \n"))
       
    if user_option == 1:
        DB.show_db_requirements()
        type_of_space = input('Write the type of space that you wish to calculate the reverberation time. \n')
        volume = float(input('What is the volume of space? \n'))
        total_absorption = [0] * 6
        
        while True:
            DB.show_db_coefficient()
            material = input('Write the material of the first surface avaiable in database \n')
            area = float(input('What is the size of surface? \n'))
            absorption = Space.absorption(area, material)
            total_absorption = np.add(absorption, total_absorption)
            
            user_input = int(input('If you finish adding surfaces press 1 \n'
                                   'If you want to add the next surface press 2 \n'))
            if user_input == 1:
                Space.calculation(volume, total_absorption, type_of_space)
                print('The reverberation time has been calculated')
                break
            elif user_input == 2:
                True
        
    elif user_option == 2:
        DB.show_db_coefficient()
        
    elif user_option == 3:
        material_name = input('Write the name of the material that you want to add \n')
        Hz125 = float(input('Write the absorption coefficent for 125 Hz \n'))
        Hz250 = float(input('Write the absorption coefficent for 250 Hz \n'))
        Hz500 = float(input('Write the absorption coefficent for 500 Hz \n'))
        Hz1000 = float(input('Write the absorption coefficent for 1000 Hz \n'))
        Hz2000 = float(input('Write the absorption coefficent for 2000 Hz \n'))
        Hz4000 = float(input('Write the absorption coefficent for 4000 Hz \n'))
        my_material = DB(material_name, Hz125, Hz250, Hz500, Hz1000, Hz2000, Hz4000 )
        my_material.write_material()
    
    elif user_option == 4:
        sys.exit()
    
    else:
        break
