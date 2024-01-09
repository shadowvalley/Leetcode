class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = []
        end_time = []
        for interval in intervals:
            start_time.append(interval[0])
            end_time.append(interval[1])
        
        start_time.sort()
        end_time.sort()

        maxRoomRequired = float("-inf")
        curRooms = 0

        j,i = 0,0
        while i < len(start_time):
            if start_time[i] < end_time[j]:
                curRooms += 1
                i+=1
            else:
                curRooms -= 1
                j+=1
            maxRoomRequired = max(maxRoomRequired, curRooms)
        return maxRoomRequired
