#slicing = create a substring by extracting elements from
#another string indexing[] or slice()
#[start:stop:step]

# name = "Bro Code"

# # first_name = name[0:3]
# first_name = name[:3]
# #the last letter is the last index + 1
# # last_name = name[4:8]
# last_name = name[:8]
# # funky_name = name[0:8:2] #every x character including the first (depends the last value)
# funky_name = name[::2]
# reversed_name = name[::-1]

# print(first_name)

# website = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7, -4)

# print(website2[slice])

#------------------------------------------
credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])

# EXERCISE 1
credit_number = "1234-5678-9012-3456"
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# EXERCISE 2
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)