import random
a = random.sample(range(1,50),10)
b = random.sample(range(1,35),5)

common = [i for i in a if i in b]
print(common)
