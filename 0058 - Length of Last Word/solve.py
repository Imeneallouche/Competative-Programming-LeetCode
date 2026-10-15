class Solution(object):
    def lengthOfLastWord(self, s):
        i=1
        while i<=len(s) and s[-i]==" ":
            i+=1
        r=i
        while i<=len(s) and s[-i]!=" ":
            i+=1
        return i-r