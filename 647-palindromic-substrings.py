class Solution(object):
    def countSubstrings(self, s):
        """
        not optimal in the general case
		time complexity is n(n+1)/2
        :type s: str
        :rtype: int
        """
        palindrome_count = 0
        backwards_s = s[::-1]
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                if s[j:j+i] == backwards_s[len(s) - j - i :len(s) - j]:
                    palindrome_count += 1
        return palindrome_count
