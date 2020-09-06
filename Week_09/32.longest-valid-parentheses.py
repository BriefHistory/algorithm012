#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0       # 最大合法长度(返回值)
        stack=[-1,]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i,ch in enumerate(s):
            if '('==ch:  # 左括号
                stack.append(i)
            elif len(stack)>1:  # 右括号，且有成对左括号
                stack.pop()     # 成对匹配
                ans = max(ans, i - stack[-1])
            else:   # 非法的右括号
                stack[0]=i
        return ans
""" #不使用stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now """
# @lc code=end

