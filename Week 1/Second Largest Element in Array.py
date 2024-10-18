class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
       
        largest = second_largest = -1
       
        for i in arr:
            if i > largest:
                largest = i
       
        for j in arr:
            if j > second_largest and j < largest:
                second_largest = j

        return second_largest
