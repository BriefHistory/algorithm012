#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        # dp[i]：以 s[i] 结尾的前缀字符串的解码个数

        # 分类讨论：
        # 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        # 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
        dp = [0 for _ in range(size)]

        if s[0] == '0':
            return 0
        dp[0] = 1

        for i in range(1, size):
            if s[i] != '0':
                dp[i] = dp[i - 1]

            num = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))

            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[size - 1]

""" class Solution:
    def numDecodings(self, s: str) -> int:
        		
		## TIME COMPLEXICITY : O(N) ##
		## SPACE COMPLEXICITY : O(N) ##
    
        
        n = len(s)        
        if n < 1: 
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1                           # 空值
        dp[1] = 0 if(s[0] == "0") else 1
        for i in range(2, n + 1):
            if 1 <= int(s[i-1 : i]) <= 10:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2 : i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]     """    
# @lc code=end

