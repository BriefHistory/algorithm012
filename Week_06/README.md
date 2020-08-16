学习笔## 动态规划
### 关键点：
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）
共性：找到重复子问题
差异性：最优子结构、中途可以淘汰次优解
### e.g.1 fibonacci数列
```python

```
### e.g.2 路径计数
**关键点**
```
1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], …)
2. 储存中间状态：opt[i]
3. 递推公式（美其名曰：状态转移方程或者 DP 方程）
Fib: opt[i] = opt[n-1] + opt[n-2]
二维路径：opt[i,j] = opt[i+1][j] + opt[i][j+1] (且判断a[i,j]是否空地）
```
### 不同路径
#### 不同路径I
[https://leetcode-cn.com/problems/unique-paths/](https://leetcode-cn.com/problems/unique-paths/)
![](DraggedImage.png)
方法二只存最近的一行（而不是方法1的二维数组）
#### 不同路径II
![高手代码](DraggedImage-1.png)

### 最长公共子序列
[https://leetcode-cn.com/problems/longest-common-subsequence/](https://leetcode-cn.com/problems/longest-common-subsequence/)
![](12%20%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6-%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5-%E8%A6%83%E8%B6%85-%E7%AC%AC%E5%8D%81%E4%BA%8C%E8%AF%BE%EF%BC%88%E6%8B%96%E7%A7%BB%E9%A1%B9%E7%9B%AE%EF%BC%89.pdf)
![python](DraggedImage-2.png)
* 疑问：
Python 如何建立二维数组？m+1  n+1 的二维数组且为0 
```python
dp = [0] * (n + 1) for _ in range (m + 1)
```


![](12%20%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6-%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5-%E8%A6%83%E8%B6%85-%E7%AC%AC%E5%8D%81%E4%BA%8C%E8%AF%BE%EF%BC%88%E6%8B%96%E7%A7%BB%E9%A1%B9%E7%9B%AE%EF%BC%89-1.pdf)
### 三角形最小路径和
![](DraggedImage-3.png)
![py3](DraggedImage-4.png)
（先纵坐标倒数第二层后 横座标）
* 国际站优秀代码
[https://leetcode.com/problems/triangle/discuss/38735/ Python-easy-to-understand-solutions-(top-down-bottom-up](https://leetcode.com/problems/triangle/discuss/38735/%20Python-easy-to-understand-solutions-(top-down-bottom-up)
### 53 最大子序列和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
![](DraggedImage-5.png)

![乘积最大子序列](DraggedImage-6.png)
### 322 零钱兑换
```python
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
```
### 198 打家劫舍
![思路1](DraggedImage-7.png)
![](DraggedImage-8.png) ![思路2](DraggedImage-9.png)
![](DraggedImage-10.png)
### 121 买卖股票最佳时机
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/)记