import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        # counter = {}
        # for num in nums:
        #     if num in counter:
        #         counter[num]+=1
        #     else:
        #         counter[num] = 1

        counter = Counter(nums)
        for key, freq in counter.items():
            heapq.heappush(heap, (-freq, key))

        topKElements = []
        while len(topKElements) < k:
            _, key = heapq.heappop(heap)
            topKElements.append(key)
        
        return topKElements
