import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        heap = []
        for char, freq in counter.items():
            heapq.heappush(heap, (-freq, char))

        frequencySortedString = ""
        while len(heap) > 0:
            freq, char = heapq.heappop(heap)
            freq = -1 * freq

            while freq > 0:
                frequencySortedString += char
                freq -= 1
        return frequencySortedString