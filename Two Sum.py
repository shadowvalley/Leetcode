class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        ans = []

        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in dict:
                ans.append(idx)
                ans.append(dict[to_find])
            else:
                dict[num] = idx
        return ans
        
