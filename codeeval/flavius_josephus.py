def flavius_josephus(test):
    num, i = [int(n) for n in test.strip().split(',')]
    i -= 1
    people = [p for p in range(num)]
    killed = []
    kill_at = i
    while len(people) > 1:
        killed.append(str(people.pop(kill_at)))
        kill_at = (kill_at + i) % len(people)


    killed.append(str(people.pop()))
    print(' '.join(killed))

print(flavius_josephus('10,3'))
