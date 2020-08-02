#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
""" 
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/jian-ji-rong-yi-li-jie-java-er-fen-fa-by-breezean/
思路
由于题目要求时间复杂度为 O(log n)，故实现为二分法查找，关于二分法，一般存在 low,high,mid位，来辅助判断。

如果 target 在[mid+1,high] 序列中，则low = mid+1,否则 high = mid,关键是如何判断 target在[mid+1,high]序列中,具体判断如下：
当[0, mid] 序列是升序: nums[0] <= nums[mid], 当target > nums[mid] || target < nums[0] ,则向后规约
当[0, mid] 序列存在旋转位: nums[0] > nums[mid],当target < nums[0] && target > nums[mid],则向后规约
当然其他其他情况就是向前规约了
循环判断，直到排除到只剩最后一个元素时，退出循环，如果该元素和 target 相同，直接返回下标，否则返回 -1。 """


""" class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[0] == target:
                return nums[0]
            elif (nums[0]<= nums[mid] & (nums[mid] < target | nums[0] > target)):
                left = mid + 1
            elif(target > nums[mid] & nums[0] > target):
                left = mid + 1
            else:
                right = mid
    return left == right & (left if nums[left] == target else -1) #需更正 """

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low = 0
        high = len(nums) - 1 

        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[high]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low =  mid + 1 
            else:
                if nums[mid] <= target <= nums[high]:
                    low =  mid + 1 
                else:
                    high = mid - 1
        return -1 



        
# @lc code=end

