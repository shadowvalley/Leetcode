class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        self.genCombs(candidates, target, ans, 0, [])

        return list(ans)

    def genCombs(self, candidates: List[int], target: int, ans, idx: int, store: List[int]):
        if target == 0:
            ans.add(tuple(store))
        elif target < 0:
            return
        else:
            # do backtrack logic
            for i in range(idx, len(candidates)):
                # Skip duplicates
                if i > idx and candidates[i] == candidates[i-1]: 
                    continue
                store.append(candidates[i]) # take
                self.genCombs(candidates, target - candidates[i], ans, i+1, store)
                store.pop() # not take
