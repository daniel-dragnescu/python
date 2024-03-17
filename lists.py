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

print(foods.index("pizza"))

for food in foods:
  print(food)