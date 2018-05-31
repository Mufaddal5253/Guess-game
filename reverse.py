import random

lower = [chr(x) for x in range(ord('a'), ord('z')+1)]
upper = [chr(x) for x in range(ord('A'), ord('Z')+1)]
special =  ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "<", ">", ",", ".", "/", "?", ";", ":", "|", "\\", "}", "\]", "\{", "[", "~", "`", "}" ]
number = range(0,9)


def generatepassword(strength = 'strong'):
    if strength == 'strong':
        specials = random.sample(special, 3)
        numbers = random.sample(number, 3)
        uppers = random.sample(upper, 5)
        lowers = random.sample(lower, 5)
        password = specials + numbers + uppers + lowers
        random.shuffle(password)
        random.shuffle(password)
        random.shuffle(password)
        return ''.join(str(x) for x in password)
    else:
        numbers = random.sample(number, 2)
        uppers = random.sample(upper, 2)
        lowers = random.sample(lower, 4)
        password = numbers + uppers + lowers
        random.shuffle(password)
        return ''.join(str(x) for x in password)


strength = ''
while strength not in ['weak', 'strong']:
    strength = input("How strong do you want your password - weak/strong: ")

print (generatepassword(strength))
