class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high - low)//2
            print("mid -> ", mid)

            if nums[mid] == target:
                return mid
            
            # search which side is sorted
            if nums[low] <= nums[mid]:
                # is key present here
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                # is key present here
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
