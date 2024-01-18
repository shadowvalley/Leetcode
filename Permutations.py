class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.getPerm(nums, [], ans)
        return ans
    
    def getPerm(self, nums, store, ans):
        if len(store) == len(nums):
            ans.append(store[:])
            return

        for i in range(len(nums)):
            if nums[i] in store:
                continue
            store.append(nums[i])
            self.getPerm(nums, store, ans)
            store.pop()
        