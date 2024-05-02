class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        s = sorted(s)
        f,l,i = s[0], s[-1],1
        while i<=min(len(f),len(l)) and l[:i]==f[:i]:           
            i+=1
        return f[:i-1]