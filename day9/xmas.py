from collections import defaultdict

class Xmas:
    def __init__(self, preamble_length):
        self.preamble_length = preamble_length

    def detect_error(self, nums):
        """
        Find the first num in nums that is not a sum of any two numbers in the previous (preamble_length) numbers
        """
        if len(nums) < self.preamble_length:
            raise ValueError('Input too short')

        # Read the preamble (stored as a map of numbers to their no. of occurrences)
        history = XmasHistory(nums[:self.preamble_length])

        # Find a num which is not the sum of any two previous nums
        for i in range(self.preamble_length, len(nums)):
            if history.contains_sum(nums[i]):
                # Update the history
                history.remove(nums[i - self.preamble_length])
                history.add(nums[i])
            else:
                # Have found an error
                return nums[i]

    def crack(self, nums, num):
        """
        Find a contiguous range of >=2 numbers in nums that add up to num, and return the sum of the min and max values
        """
        left = 0
        right = 1
        curr_sum = nums[0] + nums[1]
        while right < len(nums) - 1 and curr_sum != num:
            if curr_sum > num:
                curr_sum -= nums[left]
                left += 1
            if curr_sum < num:
                right += 1
                curr_sum += nums[right]
        contiguous_range = nums[left:right + 1]
        return min(contiguous_range) + max(contiguous_range)

class XmasHistory:
    def __init__(self, initial=[]):
        self.history = defaultdict(int)
        for num in initial:
            self.add(num)

    def add(self, num):
        self.history[num] += 1

    def remove(self, num):
        self.history[num] -= 1

    def contains_sum(self, sum_):
        """
        Checks if history contains two numbers that add up to a sum_
        """
        for num, count in self.history.items():
            complement = sum_ - num
            # If they are the same number, check that it appears at least twice
            if complement == num and count >= 2:
                return True
            elif complement in self.history:
                return True
        return False
