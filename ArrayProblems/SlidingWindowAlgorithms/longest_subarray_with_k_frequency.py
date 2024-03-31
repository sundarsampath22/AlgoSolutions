#Sliding window algorithm for determining the length of the longest subarray with maximum frequency k (no element appearing more than k times)
#
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 1
        #Keep track of our current longest subarray
        curResult = 0
        hmap = {}
        i = 0
        while i < len(nums):
            curNum = nums[i]
            if curNum in hmap:
                prevFreq = hmap[curNum]
                #case where this number invalidates our current subarray
                if prevFreq == k:
                    #move forward until we have a suitable new starting point
                    start = i - curResult
                    #need to find the earliest occurence of the curNum in our current subarray
                    #our new subarray becomes [earliestOccurenceOfCurNum+1:i+1]
                    while nums[start] != curNum:
                        num = nums[start]
                        hmap[num] = hmap[num] - 1
                        start += 1
                    #our new subarray  
                    curResult = i - start
                #case where our current subarray is still valid by including this number
                else:
                    hmap[curNum] = prevFreq + 1
                    curResult += 1
            #we haven't yet seen this number (and k >= 1) so it's guaranteed to be valid in our current subarray
            else:
                hmap[curNum] = 1
                curResult += 1
            result = max(result, curResult)
            i += 1
            
        return result