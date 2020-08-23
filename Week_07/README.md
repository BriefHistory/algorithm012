## Trie树
![](DraggedImage.png)
### 基本性质
1. 结点本身不存完整单词;
2. 从根结点到某一结点，路径上经过的字符连接起来，为该结点对应的 字符串;
3. 每个结点的所有子结点路径代表的字符都不相同。
![结点内部实现](13%20%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6-%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5-%E8%A6%83%E8%B6%85-%E7%AC%AC%E5%8D%81%E4%B8%89%E8%AF%BE%EF%BC%88%E6%8B%96%E7%A7%BB%E9%A1%B9%E7%9B%AE%EF%BC%89.pdf)
视频20:51
```python
# Python 
class Trie(object):
  
    def __init__(self): 
        self.root = {} 
        self.end_of_word = "#" 
 
    def insert(self, word): 
        node = self.root 
        for char in word: 
            node = node.setdefault(char, {}) 
        node[self.end_of_word] = self.end_of_word 
 
    def search(self, word): 
        node = self.root 
        for char in word: 
            if char not in node: 
                return False 
            node = node[char] 
        return self.end_of_word in node 
 
    def startsWith(self, prefix): 
        node = self.root 
        for char in prefix: 
            if char not in node: 
                return False 
            node = node[char] 
        return True
```
## 并查集
```python
# Python 
# 模板
def init(p): 
    # for i = 0 .. n: p[i] = i; 
    p = [i for i in range(n)] 
 
def union(self, p, i, j): 
    p1 = self.parent(p, i) 
    p2 = self.parent(p, j) 
    p[p1] = p2 
 
def parent(self, p, i): 
    root = i 
    while p[root] != root: 
        root = p[root] 
    while p[i] != i: # 路径压缩 ?
        x = i; i = p[i]; p[x] = root 
    return root
```
## A*代码模板
```python
# Python
def AstarSearch(graph, start, end):
    pq = collections.priority_queue() # 优先级 —> 估价函数
    pq.append([start]) 
    visited.add(start)
    while pq: 
        node = pq.pop() # can we add more intelligence here ?
        visited.add(node)
        process(node) 
        nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```
