class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Question Link: https://leetcode.com/problems/contains-duplicate/
        Intuition:It utilizes a set to remove duplicates from the list. By comparing the lengths of the original list and the set of unique elements,
        the function determines if there are any duplicates present. If the lengths are unequal, indicating the presence of duplicates,
        it returns True; otherwise, it returns False.
        """
        return len(set(nums)) != len(nums)
