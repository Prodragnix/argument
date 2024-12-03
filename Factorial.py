def factorial(x):
    '''Hi! Today I am going to calculate the factorial!'''
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print('The factorial of 0 is',factorial(0))
print('The factorial of 1 is',factorial(1))
print('The factorial of 5 is',factorial(5))
print('The factorial of 10 is',factorial(10))
print('The factorial of 100 is',factorial(999))
