class Solution:
    def threeSumClosest(self, n: List[int], t: int) -> int:
        n.sort()
        s = n[0]+n[1]+n[2]

        for i in range(len(n)-2):
            j,k = i+1, len(n)-1
            while j<k:
                current=n[i]+n[j]+n[k]
                if current==t:
                    return t
                elif abs(s-t)>abs(current-t):
                    s=current
                
                if current > t:
                    k-=1
                else:
                    j+=1
        return s