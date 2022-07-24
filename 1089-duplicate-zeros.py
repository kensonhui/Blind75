class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        output = [-1 for i in range(0, len(arr))]
        i = 0
        j = 0
        while j < len(arr):
            if (arr[i] != 0):
                output[j] = arr[i]
            else:
                output[j] = 0
                if (j + 1 < len(arr)):
                    output[j + 1] = 0
                j += 1
            i += 1
            j += 1
        i = 0
        while (i < len(arr)):
            arr[i] = output[i]
            i += 1
        return
