# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  _n = int(input())
  coins = list(map(int, input().split()))
  total_amount = int(input())
  
  dp = [0] * (total_amount+1)
  dp[0] = 1
  
  for coin in coins:
    for i in range(coin, total_amount+1, 1):
      dp[i] += dp[i-coin]

  print(dp[total_amount])
