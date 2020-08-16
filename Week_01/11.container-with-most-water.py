#
# @ljx app=leetcode id=11 lang=python3
#
# [283] Move Zeroes
#
# python 没有i++ 无奈
"""

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j, res = 0, len(height)-1, 0
        # 面积为minheighit* (j-i),最小值为heighit[i]或者heighi[j]
        while i < j:
            if height[i] < height[j]:
                res = max(res,height[i] * [j-i]) 
                i += 1
            else:
                res = max(res, heighit[j] * (j-i))
                j -= 1
        return res

# 优化写法 java有三元运算符，python没有，放弃




# 一维数组的数据变换,省略
""" class Solution:
    def maxArea(self,height: list[int]) -> int:
        for i in range(0, len(height)-1):
            for j in range(i+1,len(height)):
                i,j = j,i  """
""" int minHeight = a[i] < a[j] ? a[i++]:a[j --] """