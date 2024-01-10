class Solution:
    # DP
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[0] = True

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]