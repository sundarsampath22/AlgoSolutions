class Solution:
    def minSumNonUniqueSubarray(self,arr):
        minSum = float('inf')
        curSum = 0
        resLeft = None
        resRight = None
        right = 0
        pos_map = {}
        prefixSumArr = [0 for _ in range(len(arr)+1)]
        for i in range(1,len(prefixSumArr)):
            if i == 1:
                prefixSumArr[i] = arr[i-1]
            else:
                prefixSumArr[i] = prefixSumArr[i-1] + arr[i-1]
        print(prefixSumArr)
        while right < len(arr):
            curNum = arr[right] 
            if curNum in pos_map:
                left = pos_map[curNum]
                curSum = prefixSumArr[right] - prefixSumArr[left]
                curSum = sum(arr[left: right+1])
                if curSum < minSum:
                    minSum = curSum
            pos_map[curNum] = right
            right += 1
        return minSum

solution = Solution()
print(solution.minSumNonUniqueSubarray([1, 100, 1, 7, 7]))
print(solution.minSumNonUniqueSubarray([1, 2, 1, 2]))
print(solution.minSumNonUniqueSubarray([1, 2, 3, 1, 2, 1]))



