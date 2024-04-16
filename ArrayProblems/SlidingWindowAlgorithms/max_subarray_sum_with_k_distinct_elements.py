#Classic sliding window problem
#Essentially just max subarray sum with the additional constraint that every element in the subarray must be unique
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        subarray_set = set()
        left = 0
        right = 0
        curSum = 0
        maxSum = 0
        while right < len(nums):
            curNum = nums[right]
            if curNum not in subarray_set:
                subarray_set.add(curNum)
                curSum += curNum
                if len(subarray_set) == k:
                    maxSum = max(curSum, maxSum)
                    curSum -= nums[left]
                    subarray_set.remove(nums[left])
                    left += 1
            else:
                while left < right and nums[left] != nums[right]:
                    curSum -= nums[left]
                    subarray_set.remove(nums[left])
                    left += 1
                left += 1
            right += 1
        return maxSum
                
