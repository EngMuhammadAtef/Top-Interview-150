class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] != val:
                arr.append(nums[i])
                k += 1
        
        nums[:] = arr
        return k