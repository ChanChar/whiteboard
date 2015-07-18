test = '4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5'

def swap_numbers(str):
    words = str.strip().split(' ')
    swapped_words = [ word[-1] + word[1:-1] + word[0] for word in words ]
    return ' '.join(swapped_words)
