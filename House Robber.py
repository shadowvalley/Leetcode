class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        if len(nums) < 2:
            return nums[0]

        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])

        return dp[len(nums)]
        