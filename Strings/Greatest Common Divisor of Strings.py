'''
Greatest Common Divisor of Strings


For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


'''
str1 = "LEET"
str2 = "CODE"
result = "".join(dict.fromkeys(str1))
rk = ''
ko = False
for i in result:
    if i in str2:
        rk += i
        ko = True
if ko is True:
    print(rk)
else:
    print()

