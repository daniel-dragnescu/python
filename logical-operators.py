temp = int(input("What is the temperature outisde?"))

if temp >= 0 and temp <= 30:
  print("The temperature is good today")
  print("Go outside!")
elif temp < 0 or temp >= 30:
  print("The temperature is bad")
  print("Stay inside!")


if not(temp >= 0 and temp <= 30):
  print("The temperature is good today")
  print("Go outside!")
elif not(temp < 0 or temp >= 30):
  print("The temperature is bad")
  print("Stay inside!")

sunny = True

if not sunny:
  print("It's overcast.")
else:
  print("It's blistering")