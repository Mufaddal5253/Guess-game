# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# Then the program should print the dictionary.

def createdict(n):
    dictofnumbers = dict()
    for i in range(1, n):
        dictofnumbers[i] = i * i
    return dictofnumbers

a = createdict(10)
print(a)
        
    
