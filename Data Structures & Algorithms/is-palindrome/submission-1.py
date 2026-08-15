from string import ascii_lowercase
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.lower() in ascii_lowercase or i.isdigit():
                s1 += i.lower()
        return s1 == s1[::-1]