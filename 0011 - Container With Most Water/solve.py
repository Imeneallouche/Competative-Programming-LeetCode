class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        w = 0
        while i!=j:
            c = (j-i)*(min(height[j],height[i])) 
            if w<c:
                w=c
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return w