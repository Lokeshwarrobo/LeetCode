'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''
'''
Explanation :
Step 1 : Intialize variables i = 0, j = length of string - 1
Step 2 : Run a loop
Step 3 : before swapping : s[i] = h, s[j] = o
         after swapping  : s[i] = o, s[j] = h
            s = ['o', 'e', 'l', 'l', 'h']
        before swapping : s[i] = e, s[j] = l
         after swapping  : s[i] = l, s[j] = e
            s = ['o', 'l', 'l', 'e', 'h']

Step 4 : returns output

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

'''
def reversestring(s):
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s
print(reversestring(["h","e","l","l","o"]))
'''

