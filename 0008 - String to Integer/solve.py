class Solution:
    def myAtoi(self, s: str) -> int:
        s,i = s.strip(), 0
        
        while i < len(s) and (s[i].isdigit() or (s[i] in "+-" and i==0)):
            i += 1

        if any(c.isdigit() for c in s[:i]):
            m = int(s[:i])
            return m if -2**31<=m<2**31 else (int(m>0) - int(m<0))*2**31 - (m>0)
             
        else:
            return 0