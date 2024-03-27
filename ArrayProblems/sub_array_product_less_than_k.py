#sliding window algorithm where we shift right when we exceed the target product
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        curProduct = 1
        startIndex = 0
        i = 0 
        while i < len(nums):
            curNum = nums[i]
            curProduct *= curNum
            while startIndex <= i and curProduct >= k:
                curProduct = curProduct // nums[startIndex]
                startIndex += 1
            res += max(0,(i - startIndex) + 1)
            i += 1
        return res
