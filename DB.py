import mysql.connector
import sys

try:
    mydb = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
        password = 'XXX', #password to local database 'coefficient'
        database = 'coefficient'
    )
    mycursor=mydb.cursor()
except Exception as e:
    print(e)
    sys.exit()

class DB():
    def __init__(self, material_name, Hz125, Hz250, Hz500, Hz1000, Hz2000, Hz4000):
       self.material_name = material_name
       self.Hz125 = Hz125
       self.Hz250 = Hz250
       self.Hz500 = Hz500
       self.Hz1000 = Hz1000
       self.Hz2000 = Hz2000
       self.Hz4000 = Hz4000

    #method allows to add the material's coefficients
    def write_material(self): 
        sql = "INSERT INTO coefficient (MATERIAL, 125Hz, 250Hz, 500Hz, 1000Hz, 2000Hz, 4000Hz) values(%s, %s, %s, %s, %s, %s, %s)"
        val = (self.material_name, self.Hz125, self.Hz250, self.Hz500, self.Hz1000, self.Hz2000, self.Hz4000)
        mycursor.execute(sql, val)
        mydb.commit()
        print('The record has been added')

    #method that shows materials and their absorption coefficents from database
    @staticmethod 
    def show_db_coefficient():
        mycursor.execute("SELECT * FROM coefficient")
        result = mycursor.fetchall()
        for row in result:
            print(row)
            
   #method that shows spaces which the user can calculate the reverberation time
    @staticmethod  
    def show_db_requirements():
        mycursor.execute("SELECT * FROM requirements")
        result = mycursor.fetchall()
        for row in result:
            print(f"{row[1]}")
