<<<<<<< HEAD
n = int(input())
dp = [0] * (36)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    t = 0
    if i%2:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t + dp[i//2]**2
    else:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t
=======
n = int(input()) 
dp = [0] * (36)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    t = 0
    if i%2:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t + dp[i//2]**2
    else:
        for j in range(i//2):
            t += 2*dp[j]*dp[i-j-1]
        dp[i] = t
>>>>>>> cf13615b2933c8e61182ea4bc444c659e0c79e39
print(dp[n])