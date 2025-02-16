from typing import List


class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def max_len(offset1, offset2, max_l):
            max_count, count = 0, 0
            for k in range(max_l):
                if nums1[offset1 + k] == nums2[offset2 + k]:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 0
            return max(max_count, count)

        n1, n2 = len(nums1), len(nums2)
        result = 0
        for i in range(n1):
            length = min(n1 - i, n2)
            result = max(result, max_len(i, 0, length))
        for j in range(n2):
            length = min(n2 - j, n1)
            result = max(result, max_len(0, j, length))

        return result

    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     if len(nums2) > len(nums1):
    #         tmp = nums1
    #         nums1 = nums2
    #         nums2 = tmp
    #     n1, n2 = len(nums1), len(nums2)
    #     idx_dict = dict()
    #     result = 0
    #     for i in range(n2):
    #         idx_list = idx_dict.get(nums2[i], [])
    #         idx_list.append(i)
    #         idx_dict[nums2[i]] = idx_list
    #
    #     for i in range(n1):
    #         if nums1[i] not in idx_dict:
    #             continue
    #         start = i
    #         max_k = 0
    #         for start_in_n2 in idx_dict[nums1[start]]:
    #             k = 0
    #             if start + result >= n1 or start_in_n2 + result >= n2:
    #                 # current start is impossible to get common subarray length which is bigger than result
    #                 break
    #             while start + k < n1 and start_in_n2 + k < n2:
    #                 if nums1[start + k] == nums2[start_in_n2 + k]:
    #                     k += 1
    #                 else:
    #                     break
    #             max_k = max(max_k, k)
    #             result = max(result, k)
    #         if max_k > 0:
    #             i += max_k - 1
    #     return result


s = Solution()
print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3)
# print(s.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]) == 5)
# print(s.findLength([1, 0, 0, 0, 1], [1, 0, 0, 1, 1]) == 3)
