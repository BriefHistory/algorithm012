#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
""" class Solution: #经典思路写法
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []

        self.result = []
        # 之前的皇后所攻击到位置，数组或者set存
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # terminater
        if row >= n:
            self.result.append(cur_state)
            return
        #current level
        for col in range(n): #遍历列
            if col in self.cols or row + col in self.pie or row - col in self.na: # 解析几何 x+y =
                # go die
                continue
            # update the flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            # reverse
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    
    def _generate_result(self, n)
    board =[]
    for res in self.result:
        for i in res:
            board.append("." * i + "Q" + "." * (n - i -1))
    return [board[i:i + n]] for i in range(0,len(board), n)] """

 class Solution:   
    def solveNQueens(self, n: int) -> List[List[str]]:# 函数里定义子函数
        def DFS(queens, xy_dif, xy_sum): # (list,对角线)
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n): # 遍历列
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

    """ # 语法糖内置list comprehension;生成二维数组的数组 
    举例1:获取10以内的偶数
    print([x for x in range(10) if x % 2 == 0])
    语法
　　　　[返回值 for 元素 in 可迭代对象 if 条件]
　　　　使用中括号[]，内部是for循环，if条件语句可选
　　　　返回一个新的列表

　　列表解析式是一种语法糖
　　　　编译器会优化，不会因为简写而影响效率，反而因优化提高了效率
　　　　减少程序员工作量，减少出错
　　　　简化了代码，但可读性增强 """

    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result] 
           
        
# @lc code=end

