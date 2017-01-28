#4 questions
number1 = 5
number2 = 10

print (number1+number2)

#commetns added throughout script

pList = [1,2,3,4]
pList.append (5/2)
pList.append (9/2)
print(pList)

#number and string practice
word1 = "booger"
word2 = "avenue"

#slice practice
print (word1[0:3])

#counting character length practice
wordLength = len(word2)

print (wordLength)

#list practice
list1 = ["apple", "banana", "orange", "pear"]
print (list1 [1] + " " +list1 [2])

list1[0] = "pineapple"

print (list1[0]+list1[1]+list1[2])
print (list1[:2])

#append practice
list1.append("coconut")
list1.append(2*3)

print(list1)

#assignment splice practice
list1[3:4] = ["make the world a little kinder"]
print (list1)
list1[3:4] = []
print (list1)

#len list practice
print (len(list1))

fruitLength = len(list1)

print (fruitLength)

#nest list
nList1 = ["grapes", "kiwis"]
nList2 = ["carrot", "potatoes"]

produceList = [list1, nList1, nList2]
print (produceList)

print (produceList[0][1])

#while loop practice
a = 1
while a < 5000:
	print(a)
	a += a

