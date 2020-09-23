'''
Make the String Great
abBAcC

leEeetcode
'''

s = "abBAcC"

j = []


for i in range(len(s) - 1):
   if s[i] == s[i+1]:
      pass
   else:
    j.append(s[i])


print(j)
