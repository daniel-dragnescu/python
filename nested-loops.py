#The inner loop will finish all of its iterations before
#finishing one iteration of the outer loop

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#   for j in range(columns):
#     print(symbol, end="")
#   print()

  #end = this will prevent the cursor moving down to the next line
  #the nrs are on the same line
  #print() - add a new empty line for each iteration
  #4 in this case.

for x in range(3):
  for y in range(1, 10):
    print(y, end="")
  print()