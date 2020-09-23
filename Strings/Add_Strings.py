n = '54321'
k = ''
for i in range(len(n)-1):
    s = n[i]
    if s >= n[i+1]:
        s = n[i+1]
    print(s)
    k += s


print(k)

