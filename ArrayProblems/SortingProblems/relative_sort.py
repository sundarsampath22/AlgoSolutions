class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #the ordering of arr2 is used to order arr1, iterate through arr2 and
        #in a hashmap, store the position in the array as the key and the actual value that belongs there as the value
        #
        position_hmap = {}
        freq_hmap = {}
        #store the orderings as defined in arr2 in one hashmap
        for i in range(len(arr2)):
            position_hmap[i] = arr2[i]
        #store the frequencies of elements from arr1 in another hashmap
        for i in range(len(arr1)):
            num = arr1[i]
            freq_hmap[num] = freq_hmap.get(num,0) + 1
        i = 0
        j = 0
        #iterating through the different positions/order rankings (starting from 0), find the corresponding element that belongs there
        #and insert it equal to the number of times it appears in arr1
        while i < len(arr2):
            value_at_rank_i = position_hmap[i]
            arr1[j] = value_at_rank_i
            freq_hmap[value_at_rank_i] -= 1
            if freq_hmap[value_at_rank_i] == 0:
                freq_hmap.pop(value_at_rank_i)
                i += 1
            j += 1
        #place the remaining elements (not appearing in arr2) by ascending order
        for key in sorted(freq_hmap.keys()):
            while freq_hmap[key] > 0:
                arr1[j] = key
                freq_hmap[key] -= 1
                j += 1
        return arr1
        

