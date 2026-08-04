class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=''
        l=[]
        for i in s:
            if i.isalnum():
                ss+=i.lower()
        return ss==ss[::-1]

        