class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        minimum = float('inf')

        while low <= high:
            mid = low + (high - low)//2
            
            # search for which side is sorted
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid+1
            else:
                minimum = min(minimum, nums[mid])
                high = mid-1

        return minimum
        