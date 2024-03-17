#a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

# food = [["coffee", "soda", "tea"],
#         ["pizza", "hamburger", "hotdog"],
#         ["cake", "ice cream"]] #same thing as above

print(food[0][1]) #2nd value is the value inside the array
#and you can change it with another value


for collection in food:
  #print(collection) #loop through each array
  for elements in collection:
    print(elements, end=" ")
  print() #to aliniate each array on its line
  
#you can make it with sets and tuples too
  

#-----------------------------------------------
  
# 2D list of lists
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]

# 2D list of tuples
num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")]

# 2D list of sets
num_pad = [{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}]

# 2D tuple of lists
num_pad = ([1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"])

# 2D tuple of tuples
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# 2D tuple of sets
num_pad = ({1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"})

# 2D set of lists (NOT VALID)
num_pad = {[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]}

# 2D set of tuples
num_pad = {(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")}

# 2D set of sets (NOT VALID)
num_pad = {{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}}

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()