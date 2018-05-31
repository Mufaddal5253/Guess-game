inp = input('Enter a word: ')
if inp.lower() == inp[::-1].lower():
    print("{} is a palindrome!".format(inp))
else:
    print("{} is not a palindrome!".format(inp))
    
