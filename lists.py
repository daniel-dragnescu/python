#   List  = [] ordered and changeable. Duplicates OK


foods = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

foods[0] = "sushi"

#print(foods[0])
#print(foods[::2]) #every second element beginnig with i 0

#foods.append("ice cream") #add an element at the final
#foods.remove("hotdog")
#foods.pop() #remove the last element 
#foods.insert(0, "cake") #insert at index 0 cake
#foods.sort() #will sort a list alphabetically
#foods.clear() #remove all the elements of the list
#foods.reverse() #to reverse

# print(foods.index("pizza")) #return an index
# foods.count("pizza") #how many of pizza are in the array

# print(dir(foods)) #return a list of attributes and methods of an object
# print(help(foods))
# print(len(foods))
for food in foods:
  print(food)