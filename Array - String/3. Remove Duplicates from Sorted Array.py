class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                arr.append(nums[i])
        arr.append(nums[-1])
        nums[:] = arr
        return len(arr)