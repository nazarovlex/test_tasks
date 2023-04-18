class Solution:
    def find_max_interval(self, nums):
        # If array have no duplicate, return [0,0]
        if len(set(nums)) == 1:
            return [0, 0]

        # If input array is empty, return None
        elif len(nums) == 0:
            return None

        # Dict for all intervals and their length
        res = {}

        # Variable for iteration
        pos = 1

        # Iteration
        while pos < len(nums):

            # Create temporary array, which will reset every iteration.
            tmp = []

            # start determines the beginning of a strictly monotonic segment
            start = pos - 1

            # If the function is strictly decreasing
            if nums[pos] < nums[pos - 1]:
                # While the function is strictly decreasing, go through the array.
                while pos < len(nums):
                    if nums[pos] < nums[pos - 1]:
                        tmp.append(nums[pos - 1])
                        pos += 1
                    else:
                        break

            # If the function is strictly increasing
            elif nums[pos] > nums[pos - 1]:
                # While the function is strictly increasing, go through the array.
                while pos < len(nums):
                    if nums[pos] > nums[pos - 1]:
                        tmp.append(nums[pos - 1])
                        pos += 1
                    else:
                        break

            # If the function is not increasing and not decreasing
            else:
                while pos < len(nums):
                    # While the function is not increasing and not decreasing, go through the array.
                    if nums[pos] == nums[pos - 1]:
                        tmp.append(nums[pos - 1])
                        pos += 1
                    else:
                        break

            # Write down the last element after which the function has changed.
            tmp.append(nums[pos - 1])

            # Write down all the intervals on which the function did not increase and did not decrease.
            if len(set(tmp)) == 1:
                for ind, num in enumerate(tmp):
                    res[start + ind, start + ind] = 0

            # Write down all the intervals on which the function  increase and  decrease.
            else:
                res[start, pos - 1] = pos - start
        # Find the longest segment on which the function was strictly monotonic and return it.
        for k, v in res.items():
            if v == max(res.values()):
                return k


numbers = [1, 1, 1, 1, 1, 1, 1, 123123, 123123, 124124124, 214, 1]
result = Solution().find_max_interval(numbers)
print(result)