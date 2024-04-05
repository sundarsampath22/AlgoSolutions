#for all subarrays of size j in an array of integers, find the one with the smallest sum
#Solving this problem helps us easily solve another common problem that being
#for an array of integers, what is the maximum sum you can get if you are allowed the following
#1) A total of k numbers/choices
#2) Each choice must be an integer from the start or end of the array (the array bounds shift accordingly depending on your choice)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #for all subarrays of size j in arr, finds the one with the smallest sum
        def minSumSubarrayOfSizeJ(arr, j):
            l_1 = 0
            r_1 = j-1
            l_2 = l_1
            r_2 = r_1 + 1
            minSum = sum(arr[l_1:r_1+1])
            curSum = minSum
            while r_2 < len(cardPoints):
                newSum = curSum - arr[l_2] + arr[r_2]
                if newSum < minSum:
                    l_1 = l_2 + 1
                    r_1 = r_2
                    minSum = newSum
                l_2 += 1
                r_2 += 1
                curSum = newSum

            return(l_1, r_1)
        
        n = len(cardPoints)
        left, right = minSumSubarrayOfSizeJ(cardPoints, n - k)
        print(left,right)
        if n - k == 0:
            return sum(cardPoints)
        return sum(cardPoints[0:left]) + sum(cardPoints[right + 1:])