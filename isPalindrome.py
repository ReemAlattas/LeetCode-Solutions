class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        
        if ((x > 2**31 - 1) or (x < -2**31)):
            return False
        
        if (x < 10 ):
            return True
        
        rev_x = 0
        temp = x
        while (temp > 0):
            rev_x = (rev_x * 10) + (temp % 10)
            temp = temp // 10
        
        return x == rev_x
