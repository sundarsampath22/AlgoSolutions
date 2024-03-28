#sliding window algorithm for determining the length of the longest subarray with maximum frequency k (no element appearing more than k times)
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 1
        curResult = 0
        hmap = {}
        i = 0
        while i < len(nums):
            curNum = nums[i]
            if curNum in hmap:
                prevFreq = hmap[curNum]
                if prevFreq == k:
                    start = i - curResult
                    while nums[start] != curNum:
                        num = nums[start]
                        hmap[num] = hmap[num] - 1
                        start += 1
                    curResult = i - start
                else:
                    hmap[curNum] = prevFreq + 1
                    curResult += 1
            else:
                hmap[curNum] = 1
                curResult += 1
            result = max(result, curResult)
            i += 1
            
        return result