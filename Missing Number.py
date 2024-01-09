class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Appraoch -1 : Using extra space
        # states = [0]*(len(nums)+1)

        # for num in nums:
        #     states[num] = -1
        
        # missing = -1
        # for idx, state in enumerate(states):
        #     if state == 0:
        #         missing = idx
        #         break

        # return missing


        # Approach 2 : using XOR
        numXor = nums[0]
        for idx in range(1, len(nums)):
            numXor ^= nums[idx]

        idxXor = 0
        for idx in range(1, len(nums)+1):
            idxXor ^= idx

        return idxXor ^ numXor
        