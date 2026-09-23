class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s_set=set(nums)

        if len(nums) == len(s_set):
            return False
        return True