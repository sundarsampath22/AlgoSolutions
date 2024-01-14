#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#You can use the operations on either string as many times as necessary.

#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True
        dict_1 = {}
        dict_2 = {}
        for letter in word1:
            dict_1[letter] = dict_1.get(letter,0) + 1
        for letter in word2:
            dict_2[letter] = dict_2.get(letter,0) + 1
        if dict_1 == dict_2:
            return True
        if dict_1.keys() != dict_2.keys():
            return False
        letters = list(dict_1.keys())
        for i in range(len(letters)):
            cur_letter = letters[i]
            dict_1_count = dict_1[cur_letter]
            dict_2_count = dict_2[cur_letter]
            if dict_1_count < dict_2_count:
                j = i + 1
                while j < len(letters) and dict_1[letters[j]] != dict_2_count:
                    j += 1
                if j == len(letters):
                    return False
                dict_1[letters[j]] = dict_1[cur_letter]
            elif dict_2_count < dict_1_count:
                j = i + 1
                while j < len(letters) and dict_2[letters[j]] != dict_1_count:
                    j += 1
                if j == len(letters):
                    return False
                dict_2[letters[j]] = dict_2[cur_letter]
        return True
