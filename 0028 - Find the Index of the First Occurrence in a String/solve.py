class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,f,j=0,0,0
        while i<len(haystack):
            while i<len(haystack) and j<len(needle) and haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==len(needle):
                return f
            else:
                f+=1
                i,j=f,0
        return -1