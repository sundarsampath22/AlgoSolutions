#Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
#If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #treat the string as 2k chunks, reverse each of those 2k chunks'
        i = 0
        res = ''
        while i < len(s):
            start = i
            end = i + k - 1
            reversed_chunk = s[start:end+1][::-1]
            res += reversed_chunk + s[end+1:end+k+1]
            i += (2 * k)
        return res 