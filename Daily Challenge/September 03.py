class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def recurse(sub, num, length):
            if length == 0:
                results.add(sub)
            elif 0 <= num < 10:
                sub += str(num)
                recurse(sub, num+k, length-1)
                recurse(sub, num-k, length-1)
                        
        results = set()
        for i in range(1,10):
            recurse(str(i), i+k, n-1)
            recurse(str(i), i-k, n-1)
        return list(results)
