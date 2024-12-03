def cube(x):
    return x*x*x
def three(x):
    if x % 3==0:
        return cube(x)
    else:
        return False
print(three(5))
print(three(99999))