class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ord = sorted(zip(efficiency, speed), reverse=True)
        min_heap, sum_of_speed, performance = [], 0, 0
        for eff, curr_speed in ord:
            heappush(min_heap, curr_speed)
            if len(min_heap) <= k: sum_of_speed += curr_speed
            else: sum_of_speed += curr_speed - heappop(min_heap)
            performance = max(performance, sum_of_speed * eff)
        return performance % 1000000007
