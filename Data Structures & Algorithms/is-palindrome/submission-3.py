class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(x for x in s if x.isalnum()).lower() == "".join(x for x in s if x.isalnum()).lower()[::-1]