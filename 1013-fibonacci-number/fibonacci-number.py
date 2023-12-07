class Solution:
    def fib(self, n: int) -> int:
      if n == 0:
        return 0
      else:
        fibb = 1
        prev = 1
        for i in range(2,n):
          temp = fibb
          fibb += prev
          prev = temp
      return fibb