class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int("".join(map(str, digits)))
        a += 1
        digits = list(str(a))
        digits = [int(i) for i in digits]
        return digits