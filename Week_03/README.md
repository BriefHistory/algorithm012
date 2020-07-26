学习笔记
# 递归模板
```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```
![爬楼梯](DraggedImage.png)
# 分治模板（同递归）
Python 代码模板
```python
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

Java 代码模板
```java
// Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}
```
## 全排列问题
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # DFS
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
```
## 子集
![子集 递归](DraggedImage-1.png)

![子集 迭代](DraggedImage-2.png)
子集递归（回溯）
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def helper(idx, tmp):
            res.append(tmp)
            for j in range(idx, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res  
```

```python
# DFS recursively 
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res
    
def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], res)
```

子集迭代最优：
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
```
[https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/](https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/)
