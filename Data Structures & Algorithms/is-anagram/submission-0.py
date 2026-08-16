class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = []
        for char in s:
            list1.append(char)
        list2 = []
        for char in t:
            list2.append(char)
        list1.sort()
        list2.sort()
        return list1 == list2