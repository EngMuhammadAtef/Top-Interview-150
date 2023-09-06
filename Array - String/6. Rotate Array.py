class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) // 2 != len(nums) / 2:
            k %= len(nums)
            nums[:] = nums[-k:] + nums[:-k]
        else:
            k %= len(nums)
            nums[:] = nums[-k:] + nums[:-k]
