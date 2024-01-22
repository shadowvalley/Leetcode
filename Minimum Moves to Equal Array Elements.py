class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ele = min(nums)
        count = 0
        for num in nums:
            count = count + (num - min_ele)
        return count
