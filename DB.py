import mysql.connector
import sys

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # password to local database 'coefficient'
        database="coefficient",
    )
    mycursor = mydb.cursor()
except Exception as e:
    print(e)
    sys.exit()


class DbCoefficient:
    def __init__(self, material_name, Hz125, Hz250, Hz500, Hz1000, Hz2000, Hz4000):
        """
        initialization of parameters used in coefficient table in database
        (material and absorption coefficients in frequency bands)
        Args:
            material_name (str): name of the material in database
            Hz125 (float): absorption coefficient in 125 Hz
            Hz250 (float): absorption coefficient in 250 Hz
            Hz500 (float): absorption coefficient in 500 Hz
            Hz1000 (float): absorption coefficient in 1 kHz
            Hz2000 (float): absorption coefficient in 2 kHz
            Hz4000 (float): absorption coefficient in 4 kHz
        """
        self.material_name = material_name
        self.Hz125 = Hz125
        self.Hz250 = Hz250
        self.Hz500 = Hz500
        self.Hz1000 = Hz1000
        self.Hz2000 = Hz2000
        self.Hz4000 = Hz4000

    def write_material(self):
        """
        method that allows to add the materials coefficients
        """
        sql = "INSERT INTO coefficient (MATERIAL, 125Hz, 250Hz, 500Hz, 1000Hz, 2000Hz, 4000Hz) values(%s, %s, %s, %s, %s, %s, %s)"
        val = (
            self.material_name,
            self.Hz125,
            self.Hz250,
            self.Hz500,
            self.Hz1000,
            self.Hz2000,
            self.Hz4000,
        )
        mycursor.execute(sql, val)
        mydb.commit()
        print("The record has been added")

    def get_material(material_name):
        """
        method that allows to get a chosen material from database

        Args:
            material_name (str): material that user wants to use for calculation

        Returns:
            list: contains absorption coefficients to perform calculation of surface absoprtion
        """
        sql = "SELECT * FROM coefficient WHERE MATERIAL = %s"
        val = (material_name,)
        mycursor.execute(sql, val)
        my_material = mycursor.fetchall()
        out = []
        for x in my_material:
            for item in x:
                out.append(item)
        return out

    @staticmethod
    def show_db_coefficient():
        """
        method that shows materials and their absorption coefficents from database
        """
        mycursor.execute("SELECT * FROM coefficient")
        result = mycursor.fetchall()
        for row in result:
            print(row)


class DbRequirement:
    def __init__(self, space_requirement):
        """
        initialization of parameter used in the requirement table in database

        Args:
            space_requirement (str): name of the space that is under calculation
        """
        self.space_requirement = space_requirement

    def get_requirements(self):
        """
        method that allows to get reverberation time from database

        Returns:
            list: required reverberation time of the calculated type of space, used to generate charts
        """
        sql = "SELECT * FROM requirements WHERE SPACE = %s"
        val = (self,)
        mycursor.execute(sql, val)
        req = mycursor.fetchall()
        out = []
        for y in req:
            i = 2
            while i < len(y):
                out.append(y[i])
                i += 1
            return out

    @staticmethod
    def show_spaces_in_db():
        """
        method that shows list of spaces that user can calculate
        """
        mycursor.execute("SELECT * FROM requirements")
        result = mycursor.fetchall()
        for row in result:
            print(f"{row[1]}")
