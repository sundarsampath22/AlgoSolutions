#Classic Sliding Window Algorithm
#We have two pointers defining our window (left and right)
#We wait until some criteria has been met (in this case, the criterion is that sum(arr[left:right+1]) >= k)
#We shrink the window until this criterion is no longer met, while doing some additional "processing" logic
#In this case, the "processing" logic is determining if we've encountered left and right bounds that define a smaller window than previously seen
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curSum = 0
        right = 0
        res = float('inf')
        while right < len(nums):
            curNum = nums[right]
            curSum += curNum
            #Shrink the window while checking if we've encounterd a smaller window
            while curSum >= target and left < len(nums):
                res = min(res, right - left + 1)
                curSum -= nums[left]
                left += 1
            right += 1
        
        if res == float('inf'):
            return 0
        return res

