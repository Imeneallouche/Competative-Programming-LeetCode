class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashed={}
        l,result,i=0,0,0
        while i<len(s):
            if s[i] in hashed:
                result = l if result < l else result
                l = 0       
                i = hashed[s[i]]+1 if i<len(s)-1 else i
                hashed.clear()
             
            else:
                hashed[s[i]] = i
                l += 1
                i+=1
        return result