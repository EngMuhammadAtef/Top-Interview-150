class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for i, k in enumerate(nums):
            idxs[k] = i
        
        for i in range(len(nums)):
            sec_i = target - nums[i]
            
            try:
                if i != idxs[sec_i]:
                    return [i, idxs[sec_i]]
            except:
                continue
            
        