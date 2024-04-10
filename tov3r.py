f = open('test.txt')
n = int(f.readline())
end = lambda line: line[-1]
dp = [0] * n
for i in range(n):
    dp[i] = list(map(int, f.readline().split()))
dp.sort(key=end)
# durations = [ses[1] - ses[0] for ses in dp]
# print(dp)
tick = dp[0][1]
maxd = 1
day = []
day.append(dp[0])
print(dp)
for i in dp:
    if tick <= i[0]:
        maxd += 1
        tick = i[1]
        day.append(i)
print(maxd, day)
    

# cnt= 0
# n = len(a)
# i, j = 0, 0
# while i < n:
#     s = 0
#     while j < n and a[j] == a[i]:
#         s += a[j]
#         j += 1
#     cnt += 1
#     # print(i, j)
#     i = j
# print(n/cnt)
