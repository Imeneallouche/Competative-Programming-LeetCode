class Solution(object):
    def addBinary(self, a, b):
        r=""
        i,j,d=len(a)-1,len(b)-1,0
        
        if i>j:
            b = "0"*(i-j) + b
        else:
            a = "0"*(j-i) + a
            i = j

        while i>=0:
            if a[i]!=b[i]:
                r = str(1-d) + r
            else:
                r = str(d) + r
                d = int(a[i])
            i-=1
        if d==1:
            r = "1"+r
        return r