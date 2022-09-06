"""def factorial(x):
    n = 1   # this will store the factorial value
    while x > 0:
        n *= x
        x -= 1
    print(n)

def doubleFactorial(y):
    n = 1
    if y % 2 == 0:
        while y > 0:
            n *= y
            y -= 2
        print(n)
    elif y % 2 == 1:
        while y > 1:
            n *= y
            y -= 2
        print(n)"""

def solution(x):
    n = 1
    f = 1
    y = x - 1

    # Calculating double factorial of "x"
    if x % 2 == 0:
        while x > 0:
            n *= x
            x -= 2
    elif x % 2 == 1:
        while x > 1:
            n *= x
            x -= 2
    
    # Calculating double factorial of "y"
    if y % 2 == 0:
        while y > 0:
            f *= y
            y -= 2
    elif y % 2 == 1:
        while y > 1:
            f *= y
            y -= 2
    print(n/f)

solution(10000)