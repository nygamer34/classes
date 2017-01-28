class JLPerson:
	"""docstring for ClassName"""

	def __init__(self, name, weight, gender = "", aHeight = ""):
		self.name = name
		self.weight = weight
		self.gender = gender
		self.mHeight = aHeight
	def printDescription (self):
		print(self.name.upper())
		print ("Name:", self.name," Weight:", self.weight)
		print ("Gender:", self.gender, "Height:", self.mHeight)
	def gainHeightAndPrint (self, height):
		self.mHeight = height
		self.printDescription()


#this is a comment

girlsName = "Jessica Lin"
boysName = "Steven Gunther"
bunnyName = "Val"
listOfNames = (bunnyName,boysName,girlsName,4,5,6,7,8)



#print (girlsName) 
#print (boysName)
#print (listOfNames)

numbers = (5, 76, 34, 17)

people = (JLPerson(girlsName,115, "Female", 50),
	JLPerson("Steven", 220, "Male", "6 foot 3"),
	JLPerson("Bob", 1, "Male", "1 foot"))

for person in people:
	person.printDescription()



for num in numbers:
	print (num)