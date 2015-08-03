def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        else:
            seen.add(n)
            n = sum([int(i)**2 for i in str(n)])
    return True
