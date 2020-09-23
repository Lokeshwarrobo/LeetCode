'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

'''
from collections import Counter

s = 'leetcode'

k = Counter(s)

for i, j in k.items():
    if j == 1:
        print(s.index(i))
        break
    else:
        print(-1)

