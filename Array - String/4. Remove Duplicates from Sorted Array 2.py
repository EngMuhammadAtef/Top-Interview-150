class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 1
        while i < (len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
                if count > 2:
                    del nums[i]
                    count -= 1
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)