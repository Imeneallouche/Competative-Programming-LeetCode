class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows<2:
            return s
            
        r = [""]*numRows
        for i in range(len(s)):
            line = i % (2*numRows-2)
            if line<numRows:
                r[line]+=s[i]
            else:
                r[2*numRows-2-line]+=s[i]
    
        return ''.join(r)