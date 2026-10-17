class Solution(object):
    def reverseBits(self, n):
        r=""
        while n!=0:
            r+=str(n%2)
            n//=2
        r+="0"*(32-len(r)) 
        
        result,i=0,0
        while i<32:
            if r[-i-1]=="1":
                result+=2**i
            i+=1
        return result