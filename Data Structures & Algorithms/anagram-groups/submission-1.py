class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        finalList = []
        for str in strs:
            strAsList = "".join(sorted(str))
            dict[strAsList].append(str)
        for x in dict.values():
            finalList.append(x)
        return finalList