class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #cycle sort, then find the first number (positive) not in its correct position
        #cycle sort is an unstable linear time sorting algorithm that 
        i = 0
        n = len(nums)
        while i < n:
            correct_index = nums[i] - 1
            if 0 < nums[i] <= len(nums) and nums[correct_index] != nums[i]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            #we've found a number not in its correct index
            if nums[i] - 1 != i:
                return i + 1
        return len(nums) + 1