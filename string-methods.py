# STRING METHODS

# -------------------------------
# name = input("Enter your full name: ")

# phone_number = input("Enter your phone #: ")



# length = len(name) 

# index = name.find(" ") - to find a letter or anything

# name.rfind("o") - last position of "o" letter
# if can't find it, will return -1

# name = name.capitalize() - capit the first name

# name = name.upper()

# name = name.lower()

# result = name.isdigit() - if it has digits

# result = name.isalpha() - if has only letters, but without any spaces

# result = phone_number.count("1") - to count how many characters are

# phone_number = phone_number.replace("-", "") 
# first, the character that you want to replace
# second, the character that you want to replace with

#print(phone_number)

#print(name * 3) - to make it 3 times

#print(help(str)) - some methods


#        EXERCISE
# -------------------------------

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter a username: ")



# if len(username) > 12:

#    print("Your name can't be more than 12 characters")

# elif not username.find(" ") == -1:
#    #if no spaces are found, will return -1
#    #if the result is not -1, meaning we found a space

#    print("Your username can't contain spaces")

# elif not username.isalpha():

#    print("Your username can't contain digits")

# else:

#    print(f"Welcome {username}!")

