class Solution(object):
    def climbStairs(self, n):
        def comb(n, k):
            result = 1
            for i in range(1, k + 1):
                result = result * (n - i + 1) // i
            return result
        r=0
        a,b=n,0
        while a>=0:
            r+=comb(a+b, a)
            a-=2
            b+=1
        return r