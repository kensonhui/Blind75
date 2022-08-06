class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        brackets = {'{': '}', '(': ')', '[':']'}
        for i in range(0, len(s)):
            if s[i] in brackets.keys():
                queue.append(s[i])
            else:
                if len(queue) != 0 and s[i] == brackets[queue[len(queue) - 1]]:
                    queue.pop()
                else:
                    return False
                
        return len(queue) == 0 
