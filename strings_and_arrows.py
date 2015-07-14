def count_arrows(case):
    patterns = { ">>-->", "<--<<" }
    chars = list(case)
    count = 0

    for i, char in enumerate(chars):
        if i + 4 > len(chars) - 1:
            return count
        else:
            if "".join(chars[i:i+5]) in patterns:
                count += 1

    return count

print(count_arrows('<<>>--><--<<--<<>>>--><')) # returns 4
