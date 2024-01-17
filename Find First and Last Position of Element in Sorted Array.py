class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        if len(nums) == 0:
            ans.append(-1)
            ans.append(-1)
        else:
            upper_bound = self.upper_bound(nums, target)
            lower_bound = self.lower_bound(nums, target)
            bsearch = self.binarySearch(nums, target)

            if bsearch != -1:
                ans.append(lower_bound)
                ans.append(upper_bound-1)
            else:
                ans.append(-1)
                ans.append(-1)

        return ans


    def binarySearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

    def upper_bound(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = len(nums)

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] > target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


    def lower_bound(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = len(nums)

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] >= target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
