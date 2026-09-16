class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        fleets, max_time = 0, 0

        for position, speed in cars:
            time = (target-position)/speed

            if max_time < time:
                fleets+=1
                max_time = time

        return fleets
