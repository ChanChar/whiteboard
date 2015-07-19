# Given an unordered array of X of n integers.
# Find the array M where each element is the product of array x without the element.
# You may not use division.

def with_division(array):
    product = 1
    for num in array:
        product *= num
    return [product // num for num in array]

print(with_division([1, 2, 3, 5, 6]))

def without_division(array):

    products = [1] * len(array)
    lower_prod, upper_prod = 1, 1
    for i in range(0, len(array)):
        products[i] *= lower_prod
        lower_prod *= array[i]
        products[len(array) - 1 - i] *= upper_prod
        upper_prod *= array[len(array) - 1 - i]
    return products

print(without_division([1, 2, 3, 5, 6]))
