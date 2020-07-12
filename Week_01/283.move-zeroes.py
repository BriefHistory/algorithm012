#
# @ljxc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1
        return nums

