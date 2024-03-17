#SETS
#Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

foods = {"pizza", "hamburger", "hotdog", "spaghetti", "pudding"}
fruits = {"apple", "banana"}
#foods.update(fruits) #will add the fruits to foods
#print(foods.difference(fruits)) #what foods have and fruits doesn't
#print(foods.intersection(fruits))#what elements have in commun

#all_together = foods.union(fruits) #elements from both sets

# print(dir(foods)) #return a list of attributes and methods of an set
# print(help(foods))
# print(len(foods))
# print("pineapple" in foods)

print(foods)
#will show the items randomly each time you run the code
# print(foods[0]) #you can't use indexing because they are unordered

# foods.add("pineapple")
# foods.remove("apple")
# foods.pop() #remove whatever first element is 
# foods.clear()


#----------------------------------------------
  #TUPLE
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#used to group together related data

student = ("Daniel", 25, "male")

print(student.count("Daniel"))
print(student.index("male"))

for value in student:
  print(value)

if "Daniel" in student:
  print("Daniel is here")




