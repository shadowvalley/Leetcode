class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k,i = 0,0
        while i < len(nums):
            if nums[i] !=0:
                nums[k] = nums[i]
                k+=1
            i+=1

        # Set everything from k onwards to zero
        while k < len(nums):
            nums[k] = 0
            k+=1
            