class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumberic_s = ""
        s = s.lower()
        for i in range(0, len(s)):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <='9'):
                alphanumberic_s += s[i]
        return alphanumberic_s == alphanumberic_s[::-1]