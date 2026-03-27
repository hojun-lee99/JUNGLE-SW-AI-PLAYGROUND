# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

coins = [0] * n
for i in range(n):
  coins[i] = int(input())

coins.reverse()

total_coins = 0
for coin in coins:
  if(k > coin):
    total_coins += k // coin
    k = k % coin

print(total_coins)