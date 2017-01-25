class JLPerson:
	def __init__(self, name, weight, gender, height):
		self.name = name
		self.weight = weight
		self.gender = gender
		self.height = height

	def helloWorld(self):
		print("hello world")
		print("Name: ",self.name, "Weight: ", self.weight)
		print("Height: ", self.height, "Gender ", self.gender)

variable_name = ""

variable_name2 = 89

variable_name3 = JLPerson("Steve","650","Male","5")

variable_name3.helloWorld()

import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='tribalguardian')

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()