class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answerList = []
        for i in range(len(nums)):
            for x in range(i + 1, len(nums)):
                if nums[i] + nums[x] == target:
                    answerList.append(i)
                    answerList.append(x)
        return answerList