# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline

string1 = list(input().strip())
string2 = list(input().strip())

list_string1 = [0]
list_string2 = [0]
list_string1.extend(string1)
list_string2.extend(string2)

x = len(list_string1)
y = len(list_string2)

matrix = [[0 for _ in range(y)] for _ in range(x)]

for i in range(1, x):
  for j in range(1, y):
    if list_string1[i] == list_string2[j]:
      matrix[i][j] = matrix[i-1][j-1] + 1
    if list_string1[i] != list_string2[j]:
      matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[x-1][y-1])

