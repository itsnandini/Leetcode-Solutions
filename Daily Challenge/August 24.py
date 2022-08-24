class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n < 3:
            return False
        
        if not n%3:
            return self.isPowerOfThree(n/3)
        return False
