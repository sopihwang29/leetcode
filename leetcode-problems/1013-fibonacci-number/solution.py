class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0:
            return first
        elif n == 1:
            return second
        else:
            for i in range(3, n+2):
                first, second = second, first + second
        return second
