class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x, 0) + 1
            # counter for how many times each x appears
        
        finalList = []
        finalList = sorted(dict.items(), key = lambda x: x[1], reverse = True)
        top_k = finalList[:k]
        ansList = []
        for x in top_k:
            ansList.append(x[0])
        return ansList