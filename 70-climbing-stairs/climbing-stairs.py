class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            count = 2
            prev = 1
            for _ in range(3, n+1):
                temp = count
                count += prev
                prev = temp
        return count