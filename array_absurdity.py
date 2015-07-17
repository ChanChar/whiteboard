test = '20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14'

k, nums = test.strip().split(';')
k = int(k) - 1
total = sum([int(n) for n in nums.split(',')])
expected_total = k*(k+1)/2
answer = int(k - (expected_total - total))
print(answer)
