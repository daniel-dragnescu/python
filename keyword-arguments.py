#arg preceded by an identifier. The order of arg doesnt matter

def hello(first, middle, last):
  print("Hello, ", + first + middle + last)

hello(last="Dragnescu", middle="Pikachu", first="Daniel")

# ----- EXAMPLE 1 -----
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")

# ----- EXAMPLE 2 -----
for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")

# ----- EXERCISE -----
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
