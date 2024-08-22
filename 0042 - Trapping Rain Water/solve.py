class Solution:
    def trap(self, height: List[int]) -> int:
        s,sol= 0,0
        while s<len(height)-2:
            if height[s]<=height[s+1]:    
                s+=1
            else:
                e=s+1
                while height[e]<=height[e-1] and e<len(height)-1:  
                    e+=1   
                if (height[e]<height[s]):                           
                    for i in range(e+1,len(height)):
                        if height[i]>=height[s]:
                            e=i 
                            break
                        elif height[i]>=height[e]:
                            e=i
                for i in range(s+1,e):
                    if min(height[s],height[e])>height[i]:
                        sol+=min(height[s],height[e])-height[i]
                s=e
        return(sol)