def get_factorial(n):
    # n! = n * (n-1) * (n-2) * .... * 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# print(get_factorial(6))

from math import factorial
def recursive_factorial(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            recursive_factorial(together, letter + pocket)

print(recursive_factorial("abc"))