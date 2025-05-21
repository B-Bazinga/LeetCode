class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = False
        copy_nums = set()
        for i in nums:
            if i in copy_nums:
                is_duplicate = True
                return is_duplicate
            else:
                copy_nums.add(i)
        return is_duplicate
        