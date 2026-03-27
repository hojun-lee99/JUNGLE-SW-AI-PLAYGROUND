# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys
input = sys.stdin.readline

n = int(input())

memory = [0] * (n+1)

memory[1] = 1

for i in range(2, n+1):
  memory[i] = memory[i-1] + memory[i-2]

print(memory[n])