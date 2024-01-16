class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = len(nums)

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return ans
