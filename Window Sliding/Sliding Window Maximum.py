class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Question Link:
        Intution: It initializes a deque, queue, to store indices of elements in the current window, a pointer l to track the left 
        boundary of the window, and a list res to store the maximum values in each window.It iterates through the nums array using enumerate 
        to track the indices.For each element, it compares it with elements at indices stored in the deque from the right end. 
        If the current element is greater,it removes the indices from the deque until it finds a smaller or equal element.It adds the 
        current index to the deque.It removes the leftmost index from the deque if it's outside the current window.
        If the window size is reached (i + 1 >= k), it appends the maximum value in the window (at index queue[0]) to the result list 
        and moves the left pointer to the right.After iterating through the entire nums array, 
        it returns the list res containing the maximum values in each sliding window.
        """
        # Initialize a deque to store indices of elements in the current window
        queue = collections.deque()
        l = 0  # Initialize a pointer to track the left boundary of the window
        res = []  # Initialize a list to store the maximum values in each window

        # Iterate through the nums array
        for i, num in enumerate(nums):
            # Remove indices from the right end of the deque if the current element is greater than the elements at those indices
            while queue and num > nums[queue[-1]]:
                queue.pop()

            # Add the current index to the deque
            queue.append(i)

            # Remove the leftmost index from the deque if it's outside the current window
            if l > queue[0]:
                queue.popleft()

            # If the window size is reached, append the maximum value in the window to the result list
            if (i + 1) >= k:
                res.append(nums[queue[0]])
                l += 1  # Move the left pointer to the right

        return res
