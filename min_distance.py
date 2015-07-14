def friends_houses(locations):
    average = sum(locations) / len(locations)
    total = round(sum([abs(loc - average) for loc in locations]))

    print(average)
    print(total)

# test = [4, 3, 3, 5, 7]
test = [3, 20, 30, 40]
print(friends_houses(test))
