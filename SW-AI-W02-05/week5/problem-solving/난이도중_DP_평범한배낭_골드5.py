# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

stuffs = [0] * (n+1)
matrix = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
  w, v = map(int, input().split())
  stuffs[i] = (w, v)

for i in range(1, n+1):
  for j in range(1, k+1):
    prev_row = i-1
    stuff_weight = stuffs[i][0]
    stuff_value = stuffs[i][1]
    if j < stuff_weight:
      matrix[i][j] = matrix[prev_row][j]
    else:
      matrix[i][j] = max(matrix[prev_row][j], matrix[prev_row][j-stuff_weight] + stuff_value)

print(matrix[n][k])