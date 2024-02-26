import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Root!0611', #password to local database 'coefficient'
    database = 'coefficient'
)

mycursor=mydb.cursor()

class Space():
    def __init__(self,type_of_space):
        self.type_of_space = type_of_space
        #self.volume = volume
        #self.area = area
        #self.material = material
        self.absorption()
        self.calculation()

    @classmethod
    #method that returns total absorption of the space by chosing selected material from database and the size of surface
    def absorption(cls, area, material):
        sql = "SELECT * FROM coefficient WHERE MATERIAL = %s"
        val = (material,)
        mycursor.execute(sql, val)
        my_material = mycursor.fetchall()
        out = []
        for x in my_material:
            for item in x:
                out.append(item)

        x=2
        global absorption
        absorption = np.array([])
        while x < len(out):
            a = round(out[x]*area,2)
            absorption = np.append(absorption,a)
            x = x + 1
        return absorption

    #method which calculate the reverberation time and generate the chart that includes the calculated time and required time
    @classmethod
    def calculation(cls, volume, absorption, type_of_space):
        reverberation_time = []
        for i in absorption:
            reverberation_time.append(round((0.161*volume)/i,1))
        print(reverberation_time)

        sql = "SELECT * FROM requirements WHERE SPACE = %s"
        val = (type_of_space, )
        mycursor.execute(sql, val)
        req = mycursor.fetchall()
        out = []
        for y in req:
            i=2
            while i < len(y):
                out.append(y[i])
                i+=1
        x = [125, 250, 500, 1000, 2000, 4000]
        fig, ax = plt.subplots()
        ax.plot(x, out, 'r-.', label='requirements')
        ax.plot(x,reverberation_time, label = 'calculated RT')
        ax.legend(loc='upper right')
        ax.set_xscale("log")
        ax.set_xticks([125, 250, 500, 1000, 2000, 4000])
        ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
        plt.xlabel("Frequency [Hz]")
        plt.ylabel("Reverberation time [s]")
        plt.grid(True)
        plt.show()
