class Solution:
    def climbStairs(self, n: int) -> int:
        #f(n) = f(n-1) + f(n-2)
        first = 1
        second = 2
        if n <= 2:
            return n 
        for i in range(3, n+1):
            temp = second
            second = first + second
            first = temp
        return second
