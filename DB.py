import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'coefficient'
)

mycursor=mydb.cursor()

class DB():
    def __init__(self, material_name, Hz125, Hz250, Hz500, Hz1000, Hz2000, Hz4000):
       self.material_name = material_name
       self.Hz125 = Hz125
       self.Hz250 = Hz250
       self.Hz500 = Hz500
       self.Hz1000 = Hz1000
       self.Hz2000 = Hz2000
       self.Hz4000 = Hz4000

    def write_material(self):
        sql = "INSERT INTO figures(shape, first_parameter, second_parameter, third_parameter, height) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.material_name, self.Hz125, self.Hz250, self.Hz500, self.Hz1000, self.Hz2000, self.Hz4000)
        mycursor.execute(sql, val)
        mydb.commit()
        print('The record has been added')

    def show_db():
        mycursor.execute("SELECT * FROM coefficient")
        result = mycursor.fetchall()
        for row in result:
            print(row)