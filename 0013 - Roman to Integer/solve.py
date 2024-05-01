class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        replace = {'VIIII': 'IX', 'IIII': 'IV', 'LXXXX': 'XC', 'XXXX': 'XL','DCCCC': 'CM', 'CCCC': 'CD'}
        d = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        for right in replace:
            s=s.replace(replace[right], right)
        
        for c in s:
            num+=d[c]
        return num
        