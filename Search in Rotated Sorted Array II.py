class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                return True

            while low < mid and nums[low] == nums[mid]:
                low += 1

            while mid < high and nums[high] == nums[mid]:
                high -=1 

            if nums[low] <= nums[mid]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False
        