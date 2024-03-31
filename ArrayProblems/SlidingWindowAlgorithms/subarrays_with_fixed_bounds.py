#Three pointer solution
#Keep track of rightmost occurences of minK and maxK in our subarray
#Take difference between earlier of the two and start of subarray to determine how many valid subarrays we have
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        start = 0
        minKPosition = None
        maxKPosition = None
        end = 0
        res = 0
        while end < len(nums):
            curNum = nums[end]
            if curNum == minK:
                if minKPosition == None:
                    minKPosition = end
                else:
                    minKPosition = max(minKPosition, end)
            if curNum == maxK:
                if maxKPosition == None:
                    maxKPosition = end
                else:
                    maxKPosition = max(maxKPosition, end)
            if curNum < minK or curNum > maxK:
                minKPosition = None
                maxKPosition = None
                start = end + 1
            if minKPosition != None and maxKPosition != None:
                res += (min(minKPosition, maxKPosition) - start) + 1
            end += 1
        return res