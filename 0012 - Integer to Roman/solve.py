class Solution:
    def intToRoman(self, num: int) -> str:
        s,i = '', 0
        n = [1000,500,100,50,10,5,1]
        replace = {'VIIII': 'IX', 'IIII': 'IV', 'LXXXX': 'XC', 'XXXX': 'XL','DCCCC': 'CM', 'CCCC': 'CD'}
        d = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }

        while num>0:
            while i<len(n) and num>=n[i]:
                s+=d[n[i]]
                num-=n[i]
            i+=1
        
        for error in replace:
            s=s.replace(error, replace[error])

        return s