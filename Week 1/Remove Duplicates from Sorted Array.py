class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Handle the case where nums is empty
            return 0
        
        # Start with the first element
        count = 1  # There's at least one unique element
        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[i - 1]:  # Compare current with the previous element
                nums[count] = nums[i]  # Assign unique value to the next unique position
                count += 1  # Increment count of unique elements
        
        return count  # Return the count of unique elements
