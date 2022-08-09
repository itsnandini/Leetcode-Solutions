class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        kMod = int(1e9) + 7
        n = len(arr)
        dp = [1] * n
        arr.sort()
        numToIndex = {a: i for i, a in enumerate(arr)}

        for i, root in enumerate(arr):  
            for j in range(i):
                if root % arr[j] == 0:  
                    right = root // arr[j]
                    if right in numToIndex:
                        dp[i] += dp[j] * dp[numToIndex[right]]
                        dp[i] %= kMod

        return sum(dp) % kMod
