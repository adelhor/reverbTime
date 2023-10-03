from abc import ABC
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'coefficient'
)

mycursor=mydb.cursor()

class Space(ABC):

    @property
    def reverberation_time(self):
        return self._reverberation_time
    @reverberation_time.setter
    def reverberation_time(self, value):
        self._reverberation_time = round(value,1)

    def __init__(self,type_of_space,volume, area, material):
        self.type_of_space = type_of_space
        self.volume = volume
        self.area = area
        self.material = material
        self.absorption()
        self.calculation()

    def absorption(self):
        sql = "SELECT * FROM coefficient WHERE MATERIAL = %s"
        val = (self.material,)
        mycursor.execute(sql, val)
        my_material = mycursor.fetchall()
        out = []
        for x in my_material:
            for item in x:
                out.append(item)

        x=2
        global total_absorption
        total_absorption=[]
        while x < len(out):
            a = round(out[x]*self.area,2)
            total_absorption.append(a)
            x = x + 1
        print(total_absorption)

    def calculation(self):
        self.reverberation_time = (0.161*self.volume)/self.total_absorption
        print(self.reverberation_time)
