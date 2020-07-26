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
