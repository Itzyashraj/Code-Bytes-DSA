class Solution:
    def largest(self, arr : List[int]) -> int:
        maxm = 0
        for i in arr:
            if i > maxm:
                maxm=i
        return maxm
        


