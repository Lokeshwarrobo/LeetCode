'''

DI String Match

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]

'''

'''
Time Complexcity   : O(n)

'''

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        y=len(S)
        x=0
        for i in range(len(S)):
            if S[i]=='I':
                x+=1
                yield x-1
            else:
                y-=1
                yield y+1
        if S[-1]=='I':
            yield x
        else:
            yield y


