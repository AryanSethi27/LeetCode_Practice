class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in temp:
                return [temp[diff], index]
            temp[value] = index
        return []