class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.genSubsets(nums, 0, [], result)

        return result

    def genSubsets(self, nums: List[int], idx: int, ds: List[int], result: List[List[int]]) -> None:
        result.append(list(ds))

        for i in range(idx, len(nums)):
            ds.append(nums[i])
            self.genSubsets(nums, i+1, ds, result)
            ds.pop()
