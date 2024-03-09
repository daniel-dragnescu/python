import math
# # pi = 3.14

# # x = 3
# # y = 4
# # z = 5

# # # print(round(pi))
# # # print(math.ceil(pi))
# # print(math.floor(pi))
# # print(abs(pi))
# # #the absolute value of a nr. how far is from 0
# # print(pow(pi, 2))
# # print(math.sqrt(420)) #square root
# # print(max(x, y, z))
# # print(min(x, y, z))


# #------------------------------------------
# #arithmitic operations
# friends = 0

# friends = friends + 1
# friends+= 1

# friends = friends - 1
# friends -= 1

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# friends = friends ** 2
# friends **= 2

# remainder = friends % 3 
# print(remainder)

# #built-in functions

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
# result = min(x, y, z)

# print(result)

# #--------------------------
# print(math.pi)
# print(math.e)
# second_result = math.sqrt(y)
# second_result = math.ceil(x)
# second_result = math.floor(x)
# print(second_result)

# #----------- first exercise

# radius = float(input("Enter the radius of a circle:"))

# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm")



# #---------------second exercise

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area)}cm^2")

#----------- third exercise

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c} ")