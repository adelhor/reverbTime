import mysql.connector
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'coefficient'
)

mycursor=mydb.cursor()

class Space():
    def __init__(self,type_of_space,volume):
        self.type_of_space = type_of_space
        self.volume = volume
        #self.area = area
        #self.material = material
        self.absorption()
        self.calculation()

    @classmethod
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
        global total_absorption
        total_absorption=[]
        while x < len(out):
            a = round(out[x]*area,2)
            total_absorption.append(a)
            x = x + 1
        return total_absorption
        #print(total_absorption)

    def calculation(volume, total_absorption):
        reverberation_time = []
        for i in total_absorption:
            reverberation_time.append(round((0.161*volume)/i,1))
        print(reverberation_time)
        x = [125, 250, 500, 1000, 2000, 4000]
        plt.plot(x,reverberation_time)
        plt.xscale("log", base=2)
        #plt.xlim(125,4000)
        plt.xticks([125, 250, 500, 1000, 2000, 4000])
        plt.grid(True)
        plt.show()
