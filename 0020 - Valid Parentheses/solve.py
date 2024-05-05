class Solution:
    def isValid(self, s: str) -> bool:
        rev = {
            ")":"(",
            "}": "{",
            "]": "[",
        }
        if len(s)%2:
            return False
            
        i,stack= 0,""
        while i<len(s):
            if s[i] in "({[":
                stack+=s[i]
                i+=1
            else:
                if not stack:
                    return False
                
                else:
                    j=0
                    while j<len(stack) and i+j<len(s) and s[i+j] in rev and stack[len(stack)-1-j] == rev[s[i+j]]:
                        j+=1
                    stack = stack[:-j]    
                    i+=j
        if stack:
            return False
        else:
            return True