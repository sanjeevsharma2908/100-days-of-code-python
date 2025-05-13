def add(*agrs):
    sum = 0
    for i in agrs:
        sum += i
    return sum

#print(add(1,2,3,4,5))
# this an demonstration of unlimited positional arguments in python

def calculate(n, **kwargs):
    #print(kwargs)
    # for (key, value ) in kwargs.items():
    #      if key == 'add':
    #          print(add(value))
    #     if key == 'multiply':
    #         print(value * add(value))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)




calculate(2, add = 3, multiply = 5)