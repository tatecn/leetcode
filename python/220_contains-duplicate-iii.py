from typing import List


class Solution:

    def __get_index(self, num: int, size: int) -> int:
        if num >= 0:
            return num // size
        return (num + 1) // size - 1

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = dict()
        size = valueDiff + 1
        for i in range(len(nums)):
            index = self.__get_index(nums[i], size)
            if index in buckets:
                return True
            left = index - 1
            num_left = buckets.get(left, None)
            if num_left is not None and nums[i] - num_left <= valueDiff:
                return True
            right = index + 1
            num_right = buckets.get(right, None)
            if num_right is not None and num_right - nums[i] <= valueDiff:
                return True
            buckets[index] = nums[i]
            if i >= indexDiff:
                index_del = self.__get_index(nums[i - indexDiff], size)
                del buckets[index_del]

        return False

        # Time Limit Exceeded
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j < i + indexDiff + 1 and j < len(nums):
        #         if abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        #         j += 1
        # return False


s = Solution()
# print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 2, 3))  # true
print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))  # false
# print(s.containsNearbyAlmostDuplicate( [4, 1, -1, 6, 5], 3, 1))  # true
