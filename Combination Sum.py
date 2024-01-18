class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.genCombs(candidates, target, ans, 0, [])

        return ans

    def genCombs(self, candidates: List[int], target: int, ans: List[List[int]], idx: int, store: List[int]):
        if target == 0:
            ans.append(list(store))
        elif target < 0:
            return
        else:
            # do backtrack logic
            for i in range(idx, len(candidates)):
                store.append(candidates[i]) # take
                self.genCombs(candidates, target - candidates[i], ans, i, store)
                store.pop() # not take
