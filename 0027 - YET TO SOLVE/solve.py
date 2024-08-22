nums = [0,1,2,2,3,0,4,2]
val = 2

o = nums.count(val)
nums = [x for x in nums if x != val]

for i in range(o):
    nums.append('_')

print(nums)