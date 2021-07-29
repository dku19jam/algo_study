N,M=map(int,input().split())
coin=[]
dp=[10001]*10001
dp[0]=0
for _ in range(N):
    coin.append(int(input()))

for i in range(M+1):
    for j in coin:
        dp[i]=min(dp[i],dp[i-j]+1)

if dp[M]==10001:
    print(-1)
else:
    print(dp[M])

