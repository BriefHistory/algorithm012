学习笔记
# DFS
```python
#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```
# BFS
或者connection库里deque的高性能
```python
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
	...
```


```
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)

```


```
level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;
```

![](DraggedImage-3.png)
```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            child = []
            node = []
            for item in queue:
                child.append(item.val)
                if item.left:
                    node.append(item.left)
                if item.right:
                    node.append(item.right)
            result.append(child)
            queue = node
        return result
```
## 贪心算法
```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ## 先排序
        g = sorted(g)
        s = sorted(s)
        gi = si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                gi += 1
            si += 1
        return gi   # gi是得到满足的孩子序号，同时也是得到满足的孩子个数
# https://leetcode-cn.com/problems/assign-cookies/ 分发饼干，贪心机
```
## 二分查找
```python
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
```
