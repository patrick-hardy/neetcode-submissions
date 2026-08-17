class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        newList = []
        for str in strs:
            testList = "".join(sorted(str))
            if testList in dict:
                dict[testList].append(str)
            else:
                dict[testList] = [str]
        for value in dict.values():
            newList.append(value)
        return newList
        