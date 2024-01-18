import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = self.calcDistance(points)

        heap = []
        for idx, point in enumerate(points):
            heapq.heappush(heap, (distances[idx], point))

        ans = []
        while len(ans) < k:
            key, val = heapq.heappop(heap)
            ans.append(val)
        return ans
        
    def calcDistance(self, points: List[List[int]]) -> List[int]:
        distance = []
        for point in points:
            dist = math.sqrt((0-point[0])**2 + (0-point[1])**2)
            distance.append(dist)
        return distance
