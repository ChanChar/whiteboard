# def minimum_distance(test):
#     values = [int(num) for num in test.strip().split()]
#     length, house_numbers = values[0], values[1:]
#     average_distance = sum(house_numbers) // length
#     return sum([abs(house_number - average_distance) for house_number in house_numbers])
#
# def minimum_distancev2(test):
#     values = [int(num) for num in test.strip().split()]
#     length, house_numbers = values[0], values[1:]
#     middle_distance = (house_numbers[0] + house_numbers[length - 1]) // 2
#     return sum([abs(house_number - middle_distance) for house_number in house_numbers])

def minimum_distance(test):
    values = [int(num) for num in test.strip().split()]
    length, house_numbers = values[0], values[1:]
    lower, higher = min(house_numbers), max(house_numbers)
    current_min_distance = None

    for house_number in range(lower, higher):
        total = sum([abs(house - house_number) for house in house_numbers])
        if current_min_distance is None or total < current_min_distance:
            current_min_distance = total

    return current_min_distance

# Sample input: '3 3 5 6\n'
