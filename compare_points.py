def compare_points(o, p, q, r):

    if o == q:
        horizontal_dir = ''
    elif q > o:
        horizontal_dir = 'E'
    else:
        horizontal_dir = 'W'

    if r == p:
        vertical_dir = ''
    elif r > p:
        vertical_dir = 'N'
    else:
        vertical_dir = 'S'

    compass = ''.join([vertical_dir, horizontal_dir])
    return 'here' if len(compass) == 0 else compass

print(compare_points(0, 0, 1, 5))
print(compare_points(12, 13, 12, 13))
print(compare_points(0, 1, 0, 5))
