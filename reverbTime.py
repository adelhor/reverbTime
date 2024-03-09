import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
from DB import *


class Space:
    def __init__(self, volume, total_absorption, type_of_space):
        """
        parameters of space for the final calculation
        Args:
            volume (float): volume of the space - user input
            total_absorption (NDArray): calculated total absorption using absorption method
            type_of_space (str): user input
        """
        self.volume = volume
        self.total_absorption = total_absorption
        self.type_of_space = type_of_space

    @classmethod
    def absorption(cls, area, material):
        """
        method that returns surface absorption by chosing material from database and the size of the surface

        Args:
            area (float): area of the surface in the space - user input
            material (str): material of the area - user input

        Returns:
            NDArray: calculated absorption coefficiens in frequency bands
        """
        material_coefficient = DbCoefficient.get_material(material)
        x = 2
        absorption = np.array([])
        while x < len(material_coefficient):
            a = round(material_coefficient[x] * area, 2)
            absorption = np.append(absorption, a)
            x = x + 1
        return absorption

    def calculation(self):
        """
        method which calculate the reverberation time and generate the chart that includes the calculated time and required time from database
        """
        reverberation_time = []
        for i in self.total_absorption:
            reverberation_time.append(round((0.161 * self.volume) / i, 1))
        print(reverberation_time)

        requirement = DbRequirement.get_requirements(self.type_of_space)

        x = [125, 250, 500, 1000, 2000, 4000]
        fig, ax = plt.subplots()
        ax.plot(x, requirement, "r-.", label="requirements")
        ax.plot(x, reverberation_time, label="calculated RT")
        ax.legend(loc="upper right")
        ax.set_xscale("log")
        ax.set_xticks([125, 250, 500, 1000, 2000, 4000])
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        plt.xlabel("Frequency [Hz]")
        plt.ylabel("Reverberation time [s]")
        plt.grid(True)
        plt.show()
