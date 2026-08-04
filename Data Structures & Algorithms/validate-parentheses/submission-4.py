class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(" : ")", "[":"]","{":"}"}

        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if not stack or d[stack.pop()] != i:
                    return False
        return not stack

        