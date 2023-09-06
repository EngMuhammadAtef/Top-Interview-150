class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        i = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                if count > len(nums)//2:
                    return (nums[i])
                else:
                    count = 1

        if count > len(nums)//2:
            return (nums[i])
                