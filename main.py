from reverbTime import *

material = input('Write the material of the first surface \n')

area = float(input('What is the size of surface? \n'))

type_of_space = input('Write the type of space \n')

volume = float(input('What is the volume of space? \n'))

Space(type_of_space, volume, area, material)
