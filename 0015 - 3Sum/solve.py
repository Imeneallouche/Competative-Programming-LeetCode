class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol,pos,neg,z=set(),[],[],0
        for n in nums:
            if n>0:
                pos.append(n)
            elif n<0:
                neg.append(n)
            else:
                z+=1
        
        # z>2 --> [0,0,0]
        if z>2:
            sol.add((0,0,0))
        
        p,n = set(pos), set(neg)
        # -n , 0 n
        if z:
            for num in p:
                if -1*num in n:
                    sol.add((-1*num, 0 , num))
        
        for positive in p:
            for negative in n:
                k= -positive-negative
                if (k!=negative and k!=positive) or (k>0 and pos.count(k)>1) or (k<0 and neg.count(k)>1):
                    if (k>0 and k in p) or (k<0 and k in n):
                            sol.add(tuple(sorted([negative,k,positive])))
        return sol
