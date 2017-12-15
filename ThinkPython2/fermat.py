import math

def check_fermat(a, b, c, n):

    if(n > 2 and a**n  + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def prompts():

    a = int(input('Enter number a: '))
    b = int(input('Enter number b: '))
    c = int(input('Enter number c: '))
    n = int(input('Enter number n: '))

    check_fermat(a, b, c, n)


prompts()
