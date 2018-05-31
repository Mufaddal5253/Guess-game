a = input('Enter anything: ')
letters = 0
digits = 0
for x in a:
    if x.isdigit():
        digits = digits+1
    else:
        letters = letters+1

print("Letters", letters)
print("Digits", digits)

