# Count the number of prime numbers less than a non-negative number, n.
# Perfect time to use the Sieve of Eratosthenes.
def countPrimes(n):
    nums = [True] * n
    if n <= 1:
        return 0

    nums[0] = nums[1] = False
    count = 0

    for i, val in enumerate(nums):
        if val:
            count += 1
            for mark in range(i*i, n, i):
                nums[mark] = False

    return count
