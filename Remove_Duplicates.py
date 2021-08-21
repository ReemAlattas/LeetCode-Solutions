class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Return, if array is empty or contains a single element
        if n == 0 or n == 1:
            return n

        # To store index of the next unique element
        j = 0

        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1

        nums[j] = nums[n-1]
        j += 1
        return j
