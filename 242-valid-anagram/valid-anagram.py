class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=sorted(s)
        y=sorted(t)
        if len(x)!=len(y):
            return False
        for i in range(len(x)):
            if x[i]!=y[i]:
                return False
        return True
        