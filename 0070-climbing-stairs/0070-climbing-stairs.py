class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        total_ways = 0
        for x in range(n+1):  # Iterate through all possible values of x
            if (n - x)%2==0:
                # Calculate the corresponding value of y
                y = (n-x)//2
                total_ways += math.comb(x + y, x)  # Calculate the number of combinations using binomial coefficient
        return total_ways
        