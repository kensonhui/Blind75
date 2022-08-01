class Solution(object):
    def interpret(self, command):
        """
        O(n) time complexity
        :type command: str
        :rtype: str
        """
        word_map = {"G" : "G", "()": "o", "(al)": "al"}
        read_start = 0
        read_end = 1
        output = ""
        while(read_start < len(command)):
            if command[read_start:read_end] in word_map:
                output += word_map.get(command[read_start:read_end])
                read_start = read_end
            read_end += 1
        return output
