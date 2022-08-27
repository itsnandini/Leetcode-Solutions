import bisect

def csum_less_than_k(nums, k):
    ans = float('-inf')
    slist = [0]

    for x in range(1, len(nums)):
        nums[x] += nums[x-1]

    for p in nums:
        idx = bisect.bisect_left(slist, p-k)
        if idx < len(slist):
            ans = max(ans, p-slist[idx])

        bisect.insort(slist, p)

    return ans

class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        R = len(matrix)
        C = len(matrix[0])
        ans = float('-inf')
        for r in range(R):
            for c in range(1, C):
                matrix[r][c] += matrix[r][c-1]

        for left_edge in range(C):
            for right_edge in range(left_edge, C):
                ledge = lambda i: matrix[i][left_edge-1] if left_edge > 0 else 0
                one_d_array = [matrix[i][right_edge]-ledge(i) for i in range(R)]
                ans = max(ans, csum_less_than_k(one_d_array, k))

        return ans
