class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        
        curr = head
        nums = []
        while curr:
            nums.append(curr.val)
            curr = curr.next
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] != nums[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True
