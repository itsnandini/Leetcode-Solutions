import re

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        idxs = [ m.span() for m in re.finditer(r"(.)\1+", colors) ]
        min_time = sum([ sum(neededTime[a:b]) - max(neededTime[a:b]) for a, b in idxs ])
        return min_time
