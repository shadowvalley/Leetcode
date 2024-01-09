class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        store = set()
        ans = []

        for i in range(len(sorted_nums)-2, -1, -1):
            j, k = i+1, len(sorted_nums)-1

            while j<=k:
                curSum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if curSum == 0:
                    if i !=j and j != k and i!=k:
                        store.add(tuple((sorted_nums[i], sorted_nums[j], sorted_nums[k])))
                if curSum > 0:
                    k-=1
                else:
                    j+=1
        
        for tpl in store:
            ans.append(list(tpl))
        return ans