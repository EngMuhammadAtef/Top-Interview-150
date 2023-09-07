class Solution:
    def maxArea(self, arr: List[int]) -> int:
        i, j = 0, len(arr)-1
        size = 0
        while i<j:
            if arr[i] < arr[j]:
                temp = arr[i] * (j-i)
                size = temp if temp > size else size
                i += 1
            else:
                temp = arr[j] * (j-i)
                size = temp if temp > size else size
                j -= 1
        return size
    
# hight = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
# width = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# (min_hight * width)
# [1*(8-0), 7*(8-1), 3*(7-1), 8*(6-1), 4*(5-1), 5*(4-1), 2*(3-1), 6*(2-1)]
# [8, 49, 18, 40, 16, 15, 4, 6]
