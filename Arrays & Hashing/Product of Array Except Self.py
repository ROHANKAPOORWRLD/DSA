class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Question Link: https://leetcode.com/problems/product-of-array-except-self/
        Intuition: Initially, it initializes a result list, res, with all elements set to 1.
        The function then computes the prefix product of elements by iterating over the nums list, updating res accordingly.
        Afterward, it iterates backward through the list to compute the postfix product, updating both the product variable and res.
        The result list, res, thus stores the product of all elements to the left and right of each element in nums, except the element itself.
        Finally, the function returns the computed result list.
        """
        res = [1] * len(nums)
        product = 1
        # Calculates the prefix product
        for index in range(1, len(res)):
            res[index] = res[index - 1] * nums[index - 1]

        # Calculates the postfix product
        for index in range(len(res) - 2, -1, -1):
            product *= nums[index + 1]
            res[index] = res[index] * product
        return res
