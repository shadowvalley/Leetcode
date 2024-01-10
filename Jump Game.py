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


class Solution:
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        finalPos = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= finalPos:
                finalPos = i

        # if my final position has reached 0
        return True if finalPos == 0 else False
