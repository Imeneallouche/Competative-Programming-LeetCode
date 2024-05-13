class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {i: 0 for i in range(1, len(nums)+1)}
        for i in nums:
            if 0<i<=len(nums):
                d[i]=1
        i=1
        while i<=len(nums):
            if d[i]==0:
                return i
            i+=1
        return i