import sys

N=int(input())
food = list(map(int,sys.stdin.readline().split()))

for i in range(2,N):
    food[i]=max(food[i-2]+food[i],food[i-1])

print(food[N-1])

