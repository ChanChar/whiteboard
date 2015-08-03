# Given an integer, write a function to determine if it is a power of two.

def power_of_two(n)
    if n < 1:
        return False
    while n > 0:
        if n == 1:
            return True
        elif n % 2 == 0:
            n = n // 2
        else:
            return False
