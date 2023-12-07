class Solution:
    def climbStairs(self, n: int) -> int:
      mem = {}
      return self.helper(n, mem)
    def helper(self, n, mem) -> int:
      if n not in mem:
        if n == 1:
          mem[n] = 1
        elif n == 2:
          mem[n] = 2
        else:
          res = self.helper(n-1, mem) + self.helper(n-2, mem)
          mem[n] = res
      return mem[n]