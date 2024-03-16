import time

# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# for i in range(10):
#   print(i + 1) #count from 1 to 10

# for i in range(50, 100 + 1, 2):
#   print(i)

  #first nr - starting point
  #second nr - ending  point
  #third nr - how much to count: from 2 to 2 and so on


# for i in "Daniel":
#   print(i)


# for seconds in range(10, 0, -1):
#   print(seconds)
#   time.sleep(1)
# print("Happy New Year!")

# -1 will be a countdown
# sleep - will count at every one second

# ---------------- EXAMPLE 1 ----------------

for x in range(1, 11):
   print(x)

# ---------------- EXAMPLE 2 ----------------

for x in reversed(range(1, 11)):
   print(x)

print("Happy New Year!")

# ---------------- EXAMPLE 3 ----------------

for x in range(1, 11, 2):
   print(x)

# ---------------- EXAMPLE 4 ----------------

credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)

# ---------------- CONTINUE ----------------

for x in range(1, 21):
   if x == 13:
       continue
   else:
       print(x)

# ---------------- BREAK ----------------

for x in range(1, 21):
   if x == 13:
       break
   else:
       print(x)