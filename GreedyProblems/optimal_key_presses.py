#Given a string of lowercase letters, and the ability to map the letters in a dialpad, determine the minimum number of 
#presses it would take to type out that string
#Greedy algorithm that allocates the most frequent characters the lowest cost 
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        #allocate 1 to the first 9 characters with the greatest frequency
        #allocate the next 2 distinct buttons to 2
        #allocate the 
        mapping = {}
        freqMapping = {}
        for c in s:
            freqMapping[c] = freqMapping.get(c,0) + 1
        numKeys = 0
        res = 0
        for key in sorted(freqMapping.keys(), key=lambda x: -freqMapping[x]):
            numKeys += 1
            res += freqMapping[key] * max(1,ceil(numKeys / 9))
        return res