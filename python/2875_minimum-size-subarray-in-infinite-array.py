from typing import List
import math
import collections


class Solution:

    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        res, left, right = math.inf, 0, 0
        remainder = target % s
        k = target // s
        s = 0
        while right < 2 * n:
            s += nums[right % n]
            while s > remainder:
                s -= nums[left % n]
                left += 1
            if s == remainder:
                res = min(res, right - left + 1)
            right += 1
        return -1 if res == math.inf else res + k * n


# def minSizeSubarray(self, nums: List[int], target: int) -> int:
#     n = len(nums)
#     s = 0
#     suf_dict = collections.defaultdict(int)
#     suf_dict[0] = -1
#     for i in range(n - 1, -1, -1):
#         s += nums[i]
#         suf_dict[s] = n - 1 - i
#     total = s
#     res = math.inf
#     remainder = target % total + total
#     k = target // total
#     s = 0
#     for i in range(-1, 2 * n):
#         if i >= 0:
#             s += nums[i % n]
#         if remainder - s in suf_dict:
#             res = min(res, (i + suf_dict[remainder - s] + 2) % n)
#     return -1 if res == math.inf else res + k * n


# My workable version
# def minSizeSubarray(self, nums: List[int], target: int) -> int:
#     n = len(nums)
#     s = sum(nums)
#     res, left, right = math.inf, 0, 0
#     remainder = target % s
#     k = target // s
#     if remainder == 0:
#         k -= 1
#         remainder = s
#     s = 0
#     while right < 2 * n:
#         s += nums[right % n]
#         while s >= remainder and left <= right:
#             if s == remainder:
#                 res = min(res, right - left + 1 + k * n)
#             s -= nums[left % n]
#             left += 1
#         right += 1
#     return -1 if res == math.inf else res

# Time Limit Exceeded
# def minSizeSubarray(self, nums: List[int], target: int) -> int:
#     n = len(nums)
#     s = sum(nums)
#     res, left, right = math.inf, 0, 0
#     k = math.ceil(target / s)
#     maxi = (k << 1) * n
#     s = 0
#     while right < maxi:
#         s += nums[right % n]
#         while s >= target and left <= right:
#             if s == target:
#                 res = min(res, right - left + 1)
#             s -= nums[left % n]
#             left += 1
#         right += 1
#     return -1 if res == math.inf else res

# V1 version and has a bug
# def minSizeSubarray(self, nums: List[int], target: int) -> int:
#     n = len(nums)
#     s = 0
#     pre_sum, suf_sum = [0] * n, [0] * n
#     for i in range(n):
#         s += nums[i]
#         pre_sum[i] = s
#     suf_sum[0] = s
#     for i in range(1, n):
#         suf_sum[i] = s - pre_sum[i - 1]
#     res, left, right = math.inf, 0, 0
#     k = math.ceil(target / s)
#     maxi = (k + 1) * n if k > 0 else 2 * n
#     s = 0
#     while right < maxi:
#         curk = right // n
#         if right < n:
#             s = suf_sum[left] - (suf_sum[right + 1] if right != n - 1 else 0)
#         elif left < n:
#             s = suf_sum[left] + pre_sum[right % n] + (curk - 1 if curk > 0 else 0) * suf_sum[0]
#         else:
#             s = ((pre_sum[left % n - 1] if left % n > 0 else 0) + pre_sum[right % n] +
#                  (curk - 1 if curk > 0 else 0) * suf_sum[0])
#         # while (s >= target or (target - s) % pre_sum[n - 1] == 0) and left <= right:
#         #     if s == target or (target - s) % pre_sum[n - 1] == 0:
#         #         res = min(res, right - left + 1 + (target - s) // pre_sum[n - 1])
#         while s >= target and left <= right:
#             if s == target:
#                 res = min(res, right - left + 1)
#             s -= nums[left % n]
#             left += 1
#         right += 1
#     return -1 if res == math.inf else res


s = Solution()
print(s.minSizeSubarray([2, 3, 2, 3, 1], 5) == 2)
print(s.minSizeSubarray([1, 1, 1, 2, 3], 4) == 2)
print(s.minSizeSubarray([2, 4, 6, 8], 3) == -1)
print(s.minSizeSubarray([2, 1, 5, 7, 7, 1, 6, 3], 39) == 9)
print(s.minSizeSubarray([1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1], 83) == 53)
print(s.minSizeSubarray([1, 2, 3, 2, 1, 5, 3, 4, 5], 53) == 19)
print(s.minSizeSubarray([1, 6, 5, 5, 1, 1, 2, 5, 3, 1, 5, 3, 2, 4, 6, 6], 56) == 16)
print(s.minSizeSubarray([1, 2], 72) == 48)
