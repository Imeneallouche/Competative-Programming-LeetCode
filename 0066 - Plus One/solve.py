class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i>=0 and digits[i] == 9:
            digits[i]=0
            i -= 1
        if(i>=0):
            digits[i] = digits[i] + 1
        else:
            digits.append(0)
            digits[0]=1
        return digits