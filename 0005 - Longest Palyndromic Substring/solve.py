class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center(s: str, l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1


        begin,end = 0,0

        for i in range(len(s)):
            odd = center(s, i, i)
            even = center(s, i, i + 1)
            length = max(odd, even)
            
            if length > end - begin:
                begin = i - (length - 1) // 2
                end = i + length // 2
        
        return s[begin:end+1]



