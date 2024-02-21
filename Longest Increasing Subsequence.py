class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1

        # find max value 
        maxVal = -1
        for i in range(len(dp)):
            if dp[i] > maxVal:
                maxVal = dp[i]
        return maxVal 