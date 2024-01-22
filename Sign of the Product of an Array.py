class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = False
        prod = 1
        for num in nums:
            prod *= num

        if prod == 0:
            return 0
        elif prod < 0:
            return -1
        else:
            return 1