'''
终止条件，根据奇数偶数分解子问题，合并
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def result(N):
            if N == 0:
                return 1.0
            y = result(N // 2)
            return y * y if N % 2 == 0 else  y * y * x
        return result(n) if (n >= 0) else 1.0 / result(-n)
            

