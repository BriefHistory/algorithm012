学习笔记

## 位运算
### 指定位置的位运算
1. 将 x 最右边的 n 位清零：x & (0 << n)
2. 获取 x 的第 n 位值（0 或者 1）： (x \>\> n) & 1
3. 获取 x 的第 n 位的幂值：x & (1 \<\< n)
4. 仅将第 n 位置为 1：x | (1 \<\< n)
5. 仅将第 n 位置为 0：x & ( (1 << n))
6. 将 x 最高位至第 n 位（含）清零：x & ((1 \<\< n) - 1)
### 实战位运算要点
• 判断奇偶：
x % 2 == 1 —\> (x & 1) == 1
x % 2 == 0 —\> (x & 1) == 0
• x \>\> 1 —\> x / 2.
即： x = x / 2; —\> x = x \>\> 1;
mid = (left + right) / 2; —\>
mid = (left + right) \>\> 1;
• X = X & (X-1) 清零最低位的 1
• X & -X =\> 得到最低位的 1
• X & X => 0
### N皇后位运算
```python
# Python
def totalNQueens(self, n): 
	if n < 1: return [] 
	self.count = 0 
	self.DFS(n, 0, 0, 0, 0) 
	return self.count
def DFS(self, n, row, cols, pie, na): 
	# recursion terminator 
	if row >= n: 
		self.count += 1 
		return
	bits = (~(cols | pie | na)) & ((1 << n) — 1)  # 得到当前所有的空位
	while bits: 
		p = bits & —bits # 取到最低位的1
		bits = bits & (bits — 1) # 表示在p位置上放入皇后
		self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) 
        # 不需要revert  cols, pie, na 的状态
```

数组
![](DraggedImage.tiff)
### LRU
示例1:
```python
# Python 

class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```
实际
```python
#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

""" class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False) """


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


```
