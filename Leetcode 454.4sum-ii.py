"""
454.四数相加 II
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
 1.0 <= i, j, k, l < n
 2.nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
示例：
    输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
    输出：2
    解释：
        两个元组如下：
        1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        res = 0
        n = len(nums1)
        map = dict()
        for i in range(n):
            for j in range(n):
                key = nums1[i]+nums2[j]
                if key in map:
                    map[key] += 1
                else:
                    map[key] = 1
        for k in range(n):
            for l in range(n):
                key = -(nums3[k]+ nums4[l])
                if key in map:
                    res += map[key]
        return res
