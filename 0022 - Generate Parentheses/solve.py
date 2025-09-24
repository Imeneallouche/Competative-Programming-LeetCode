class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def backtrack(s, o, c):
            if len(s) == 2 * n:
                res.append(s)
                return
            if o < n:
                backtrack(s + "(", o + 1, c)
            if c < o:
                backtrack(s + ")", o, c + 1)
        backtrack("", 0, 0)
        return res
