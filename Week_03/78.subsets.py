class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
"""
# 更优写法，但理解有难度
 class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(idx, tmp):
            res.append(tmp)
            for j in range(idx, n):
                helper(j + 1,tmp + [nums[j]] )# tmp + [nums[j]] 这个会产生一个全新数组（copy出来的），然后传到下一次函数调用的参数。每次创建新的数组，所以就不需要进行reverse了
        helper(0, [])
        return res  
 """
# # 迭代
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
        
#         def helper(idx, tmp):
#             res.append(tmp)
#             for j in range(idx, n):
#                 helper(j + 1,tmp + [nums[j]] )
#         helper(0, [])
#         return res  
# 递归回溯


# class Solution:# 迭代官方
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
        
#         def helper(i, tmp):
#             res.append(tmp)
#             for j in range(i, n):
#                 helper(j + 1,tmp + [nums[j]] )
#         helper(0, [])
#         return res  
