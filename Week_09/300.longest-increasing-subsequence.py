#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
""" # https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/chuan-shang-yi-fu-wo-jiu-bu-ren-shi-ni-liao-lai-li/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return  ans  """
       

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []#前i个元素，以第i个数字结尾（一定包含i）的子长上升子序列的长度
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)# dp[i] = dp[j] + 1 (其中 i > j, nums[i] > nums[j])
        return max(dp)

# @lc code=eni

