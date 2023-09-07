class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:

        arr = sorted(arr1+arr2) # O(nlogn)

        if len(arr)%2 == 1:
            return(arr[ len(arr)//2 ]) # 1 2 3 4 5

        else:
            return( (arr[ len(arr)//2 -1 ] + arr[ len(arr)//2 ]) / 2 ) # 1 2 3 4