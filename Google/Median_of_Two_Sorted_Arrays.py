class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        
        print(len(nums))
        if len(nums) % 2 != 0:
            print("Odd => 1 value")
            res = nums[len(nums)//2]
        else:
            print("Even => Avg of 2 values")
            res = (nums[len(nums)//2] + nums[(len(nums)//2)-1]) / 2.0
        
        return res

# import statistics
# res = statistics.median(nums)

# The overall run time complexity should be O(log (m+n)).