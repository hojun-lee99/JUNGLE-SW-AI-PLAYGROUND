# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

num = int(input())

memo = [0] * (num+1)
memo[0] = 1
memo[1] = 1

for i in range(2, num+1):
  memo[i] = (memo[i-1] + memo[i-2]) % 15746

print(memo[num])