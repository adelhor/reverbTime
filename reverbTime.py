from abc import ABC

class Space(ABC):

    @property
    def reverberation_time(self):
        return self._reverberation_time
    @reverberation_time.setter
    def reverberation_time(self, value):
        self._reverberation_time = round(value,1)

    def __init__(self,type_of_space,volume, area, coefficient):
        self.type_of_space = type_of_space
        self.volume = volume
        self.area = area
        self.coefficient = coefficient

    def calculation(self):
        self.reverberation_time = (0.161*self.volume)/(self.area*self.coefficient)
