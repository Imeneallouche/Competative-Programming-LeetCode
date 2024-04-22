class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            r = -int(str(x)[:0:-1])
            return r if r >= -2**31 else 0
        else:
            r = int(str(x)[::-1])
            return r if r < 2**31 else 0