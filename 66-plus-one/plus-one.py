class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str, digits)))
        a += 1
        res = list(str(a))
        res = [int(i) for i in res]
        return res