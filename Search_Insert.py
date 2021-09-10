class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Lower and upper bounds
        start = 0
        end = len(nums) - 1
 
        # Traverse the search space
        while start <= end:
 
            mid =(start + end)//2
 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid-1
 
        # Return the insert position
        return end + 1
