def hamming_weight(n):
    ones = 0
    for i in str(bin(n)):
        if i == '1':
            ones += 1
    return ones

def hamming_weight_v2(n):
    return str(bin(n)).count('1')
