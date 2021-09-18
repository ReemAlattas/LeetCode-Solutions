class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trim spaces from both sides
        s = s.strip()
        
        # Split the string into a list of words by space
        ls = list(s.split(" "))
        return len(ls[-1])
