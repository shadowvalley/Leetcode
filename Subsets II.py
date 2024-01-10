class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = set()
        self.genSubsets(nums, 0, [], temp)

        return list(temp)

    def genSubsets(self, nums: List[int], idx: int, ds: List[int], result: set) -> None:
        result.add(tuple(ds))
        for i in range(idx, len(nums)):
            ds.append(nums[i])
            self.genSubsets(nums, i+1, ds, result)
            ds.pop()
