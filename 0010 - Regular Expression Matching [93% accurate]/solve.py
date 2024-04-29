class Solution:
    def isMatch(self,s: str, p: str) -> bool:
        def partition(p):
            d, current = [], ''
            for c in p:
                if c==current or c == '*':
                    l = len(d)-1 if len(d)>0 else 0
                    d[l] += c
                else:
                    d.append(c)
                    current = c
            return d

        cond = partition(p)
        i,j = 0,0

        while i<len(s) and j<len(cond):
            if "*" in cond[j]:
                # "c*"
                if cond[j][0].isalpha():
                    char = cond[j][0]
                    m = len(cond[j]) - 2*cond[j].count("*") # le minimum

                    while i<len(s) and s[i] == char:
                        i+=1
                        m-=1
                
                    if m>0:
                        return False
            
                # ".*" "..*" 
                else:
                    if j==len(cond)-1:
                        return True
                
                    while i<len(s):
                        if self.isMatch(s[i:], cond[j+1:]):
                            return True
                        else:
                            i+=1
                     
            # oulach * donc comparision one by one
            else:
                for k in cond[j]:
                    if i<len(s) and (k == s[i] or k=="."):
                        i+=1
                
                    else:
                        return False
        
            j+=1
        
        if i>= len(s) and j>= len(cond):
            return True
    
        else:
            return False