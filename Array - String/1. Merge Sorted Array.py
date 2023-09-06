class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = nums1[:m]
        i, j = 0, 0
        while i < len(arr) and j < len(nums2):
            if arr[i] < nums2[j]:
                i += 1
            else:
                arr.insert(i, nums2[j])
                j += 1

        arr += nums2[j:]
        nums1[:] = arr
        