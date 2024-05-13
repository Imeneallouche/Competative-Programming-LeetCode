class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        i,c=0,1
        while i<len(nums):
            if nums[i]>0:
                if nums[i]!=c:
                    return c
                c+=1
            i+=1
        if i==len(nums):
            return c