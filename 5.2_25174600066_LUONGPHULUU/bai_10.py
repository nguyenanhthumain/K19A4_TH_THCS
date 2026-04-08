import random
lst = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]
num = random.choice(lst)
print(num)