class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [[0 for _ in range(2)] for _ in range(len(position))]
        
        for i, p in enumerate(position):
            distance[i][0] = abs(target-p)
            distance[i][1] = speed[i]
        
        distance.sort(key=lambda x: x[0])

        fleet_count = 1
        t = distance[0][0]/distance[0][1]
        for i in range(1, len(distance)):
            d, s = distance[i]
            if t < (d/s):
                fleet_count+=1
                t = d/s

        return fleet_count
