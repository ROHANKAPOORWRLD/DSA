class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Question Link: https://leetcode.com/problems/top-k-frequent-elements/
        Intuition: Initially, it counts the frequency of each element using a defaultdict.
        Then, it creates a frequency map where each index corresponds to the frequency of elements.
        Elements are appended to the list at the index representing their frequency. The function iterates through the reversed frequency map,
        starting from the highest frequencies, and appends the elements to the result list until it reaches k elements.
        Finally, it returns the result list containing the top k frequent elements.
        """
        # Count the frequency of each element
        num_freq = collections.defaultdict(int)
        for num in nums:
            num_freq[num] += 1

        # Map frequency to the index
        freq_map = [[] for _ in range(len(nums))]
        for num, freq in num_freq.items():
            freq_map[freq - 1].append(num)

        # Iterate through the reversed freq_map as the numbers with the highest frequencies are at the end
        result = []
        for freq_list in reversed(freq_map):
            for num in freq_list:
                result.append(num)
                if len(result) >= k:
                    return result
        return result
