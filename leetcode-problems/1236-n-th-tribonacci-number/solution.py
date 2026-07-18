class Solution:
    def tribonacci(self, n: int) -> int:
        zero = 0
        first = 1
        second = 1
        if n == 0:
            return zero
        elif n == 1 or n == 2:
            return 1
        else:
            for i in range(n-2):
                zero, first, second = first, second, zero + first + second
        return second
