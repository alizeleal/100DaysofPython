import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randomPick = random.randint(0, 4)

print(friends[randomPick])

#other way to do it

print(random.choice(friends))