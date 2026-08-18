class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(x for x in s if x.isalnum()).lower()
        revString = s[::-1]
        revString = "".join(c for c in revString if c.isalnum()).lower()
        
        print(revString)
        
        return s == revString