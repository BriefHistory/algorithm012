学习笔记
### 编辑距离

### 高级字符串算法

#### 不同子序列33min
#### 最长上升子序列
* 按照动态规划定义状态的套路，我们有两种常见的定义状态的方式：本次使用第二个
dp[i] : 以 i 结尾（一定包括 i）所能形成的最长上升子序列长度, 答案是 max(dp[i])，其中 i = 0,1,2, ..., n - 1
dp[i] : 以 i 结尾（可能包括 i）所能形成的最长上升子序列长度，答案是 dp[-1] （-1 表示最后一个元素）
* 状态转移方程
由于 dp[j] 中一定会包括 j，且以 j 结尾， 那么 nums[j] 一定是其所形成的序列中最大的元素，那么如果位于其后（意味着 i > j）的 nums[i] > nums[j]，那么 nums[i] 一定能够融入 dp[j] 从而形成更大的序列，这个序列的长度是 dp[j] + 1。因此状态转移方程就有了：dp[i] = dp[j] + 1 (其中 i > j, nums[i] > nums[j])
```python
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

