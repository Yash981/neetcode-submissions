class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for i in s:
            if 'a' <= i <= 'z':
                stack.append(i)
            elif 'A' <= i <= "Z":
                stack.append(i.lower())
            elif i.isdigit():
                stack.append(i)
        # print(stack)
        news = "".join(stack)
        # print(news)
        return news == news[::-1]