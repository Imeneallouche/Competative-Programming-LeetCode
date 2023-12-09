class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed={}
        for i in range(len(nums)):
            hashed[nums[i]] = i
        
        i=0
        for n1 in nums:
            n2 = target - n1
            if n2 in nums and i != hashed[n2]:
                return [i, hashed[n2]]
            i+=1
        return []