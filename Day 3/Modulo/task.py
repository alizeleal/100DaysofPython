number = int(input("type the desired number: "))
modulo = number % 2

if modulo == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is odd")