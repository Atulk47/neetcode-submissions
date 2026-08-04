class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = len(s1)
        d = sorted(s1)

        for l in range(len(s2) - c + 1):
            b = sorted(s2[l:l + c])
            if b == d:
                return True

        return False
