#given an array of numbers, you are allowed, in one operation, to remove either two or three occurences of a particular value
#determine the minimum number of operations requried to empty the array (or -1 if it is not possible)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #keep frequency counts, and greedily remove in maximal incrememnts of 3s and 2s (respectively)
        #O(n) run time with o(n) space
        frequency_hmap = {}
        for num in nums:
            frequency_hmap[num] = frequency_hmap.get(num, 0) + 1
        res = 0
        for frequency in frequency_hmap.values():
            if frequency == 1:
                return -1
            if frequency % 3 == 0:
                res += frequency // 3
            else:
                res += ((frequency // 3) - 1) + 2
        return res