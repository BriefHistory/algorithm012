学习笔记
### 第五课
**哈希表、映射、集合**
**哈希表** (Hash Table)，也叫 **散列表**，是根据关键码值(Key Value)而直接进行访问的数据结构。 它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。 这个映射函数叫作 **散列函数** (Hash Function)，存放记录的数组叫作 **哈希表** (或散列表)。
**工程实践**
* 电话号码簿
* 用户信息表
* 缓存(LRU Cache)
* 键值对存储(Redis)
**映射 (Map)**
**集合 (Set)**
### 第六课
**树、二叉树、二叉搜索树**
* 前序知识回顾： 链表等一维结构
* 单链表 Linked List
* 树 Tree
* 二叉树 Binary Tree
* 图 Graph
**Linked List 是特殊化的 Tree**
**Tree 是特殊化的 Graph**
**二叉树遍历 Pre-order/In-order/Post-order**
1. 前序(Pre-order):根-左-右
2. 中序(In-order):左-根-右
3. 后序(Post-order):左-右-根


```python
def isAnagram(self, s: str, t: str) -> bool:
    # 定义默认布尔值参与后续运算
    result = True
    # 利用 Python 数据结构 set 去重去序
    set_tmp = set(s)
    # 先判断组成字符串的各个字符元素是否一致
    if set_tmp == set(t):
        for i in set_tmp:
            # 利用逻辑运算符判断各个字符元素的数量一致，均为 True 才输出 True
            result = result and (s.count(i) == t.count(i))
    else:
        result = False
    return (result)

```
## 树
```python
class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left, self.right = None, None
```
1.前序（Pre-order）：根-左-右
2.中序（In-order）：左-根-右
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        #  中序递归 
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

```
3.后序（Post-order）：左-右-根

## hash two sum
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) ->List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
```
## 二叉堆(需要消化)
```java
import java.util.Arrays;
import java.util.NoSuchElementException;


public class BinaryHeap {


    private static final int d = 2;
    private int[] heap;
    private int heapSize;


    /**
     * This will initialize our heap with default size.
     */
    public BinaryHeap(int capacity) {
        heapSize = 0;
        heap = new int[capacity + 1];
        Arrays.fill(heap, -1);
    }


    public boolean isEmpty() {
        return heapSize == 0;
    }


    public boolean isFull() {
        return heapSize == heap.length;
    }




    private int parent(int i) {
        return (i - 1) / d;
    }


    private int kthChild(int i, int k) {
        return d * i + k;
    }


    /**
     * Inserts new element in to heap
     * Complexity: O(log N)
     * As worst case scenario, we need to traverse till the root
     */
    public void insert(int x) {
        if (isFull()) {
            throw new NoSuchElementException("Heap is full, No space to insert new element");
        }
        heap[heapSize] = x;
        heapSize ++;
        heapifyUp(heapSize - 1);
    }


    /**
     * Deletes element at index x
     * Complexity: O(log N)
     */
    public int delete(int x) {
        if (isEmpty()) {
            throw new NoSuchElementException("Heap is empty, No element to delete");
        }
        int maxElement = heap[x];
        heap[x] = heap[heapSize - 1];
        heapSize--;
        heapifyDown(x);
        return maxElement;
    }


    /**
     * Maintains the heap property while inserting an element.
     */
    private void heapifyUp(int i) {
        int insertValue = heap[i];
        while (i > 0 && insertValue > heap[parent(i)]) {
            heap[i] = heap[parent(i)];
            i = parent(i);
        }
        heap[i] = insertValue;
    }


    /**
     * Maintains the heap property while deleting an element.
     */
    private void heapifyDown(int i) {
        int child;
        int temp = heap[i];
        while (kthChild(i, 1) < heapSize) {
            child = maxChild(i);
            if (temp >= heap[child]) {
                break;
            }
            heap[i] = heap[child];
            i = child;
        }
        heap[i] = temp;
    }


    private int maxChild(int i) {
        int leftChild = kthChild(i, 1);
        int rightChild = kthChild(i, 2);
        return heap[leftChild] > heap[rightChild] ? leftChild : rightChild;
    }


    /**
     * Prints all elements of the heap
     */
    public void printHeap() {
        System.out.print("nHeap = ");
        for (int i = 0; i < heapSize; i++)
            System.out.print(heap[i] + " ");
        System.out.println();
    }


    /**
     * This method returns the max element of the heap.
     * complexity: O(1)
     */
    public int findMax() {
        if (isEmpty())
            throw new NoSuchElementException("Heap is empty.");
        return heap[0];
    }


    public static void main(String[] args) {
        BinaryHeap maxHeap = new BinaryHeap(10);
        maxHeap.insert(10);
        maxHeap.insert(4);
        maxHeap.insert(9);
        maxHeap.insert(1);
        maxHeap.insert(7);
        maxHeap.insert(5);
        maxHeap.insert(3);


        maxHeap.printHeap();
        maxHeap.delete(5);
        maxHeap.printHeap();
        maxHeap.delete(2);
        maxHeap.printHeap();
    }
}
```
