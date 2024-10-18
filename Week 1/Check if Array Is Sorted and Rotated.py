class Solution:
    def check(self, nums: List[int]) -> bool:
        counter = 0
        n = len(nums)

        # Basically in sorted array, left -> right elements on right will be greater than left
        # Counting the number of jump downs. Ex : [3,4,5,1,2] from 5 -> 1 is the only jump down
        # There should either be no jump downs or only one jump down in array traversal (due to shift)
        for i in range(0, n-1):
            if nums[i] > nums[i+1]:
                counter += 1
        
        # In the case where the jump down exists at the edge of the shifted array. Ex: [2,1,3,4]
        if nums[-1] > nums[0]:
            counter += 1
        if (counter == 0 or counter == 1):
            return True
        return False
