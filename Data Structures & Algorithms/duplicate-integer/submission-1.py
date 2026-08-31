class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        # s=set()
        # for n in nums:
        #     if n in s:
        #         return True
        #     s.add(n)
        # return False
        