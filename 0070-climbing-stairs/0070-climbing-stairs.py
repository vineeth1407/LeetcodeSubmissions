class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        total_ways = 0
        for x in range(n // 2 + 1):  # Iterate through all possible values of x
            y = n - 2 * x  # Calculate the corresponding value of y
            total_ways += math.comb(x + y, x)  # Calculate the number of combinations using binomial coefficient
        return total_ways
        