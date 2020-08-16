#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
        
# @lc code=end

""" #跳跃游戏II https://leetcode-cn.com/problems/jump-game-ii 跳跃游戏II
class Solution:
    def jump(self, nums: List[int]) -> int:
        step=0
        end=0
        max_bound=0
        for i in range(len(nums)-1):
            max_bound=max(max_bound,nums[i]+i)
            if(i==end):
                step+=1
                end=max_bound
        return step """