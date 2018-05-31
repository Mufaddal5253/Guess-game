import random as rn
list1 = rn.sample (range(36), 12)
list2 = rn.sample (range(48), 16)
commonnums = set(list1).intersection(list2)

print(commonnums)
