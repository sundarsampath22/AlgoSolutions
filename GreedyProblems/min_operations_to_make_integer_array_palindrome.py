#Given an integer array, determine the minimum number of operations you can make to turn the array into a palindrome
#An operation here is defined as summing two consecutive elements in the array
#Greedy algorithm with two pointers; perform a sum operation on one side as soon as it results in a match with the sum/value on the other
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        startingLeft = 0
        startingRight = len(nums) - 1
        left = 0
        right = len(nums) - 1
        leftSum = nums[left]
        rightSum = nums[right]
        res = 0
        while left < right:
            if leftSum == rightSum:
                res += abs(left-startingLeft)
                res += abs(right-startingRight)
                left += 1
                right -= 1
                if left < len(nums):
                    leftSum = nums[left]
                if right >= 0:
                    rightSum = nums[right]
                startingLeft = left
                startingRight = right
            elif leftSum > rightSum:
                right -= 1
                if right >= 0:
                    rightSum += nums[right]
            else:
                left += 1
                if left < len(nums):
                    leftSum += nums[left]
        return res + abs(startingRight-right) + abs(startingLeft-left)

