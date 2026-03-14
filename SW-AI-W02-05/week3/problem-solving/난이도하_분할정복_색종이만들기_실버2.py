# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline

white_count = 0
blue_count = 0

def is_same(matrix:list, row_start:int, row_end:int, col_start:int, col_end:int):
  first_element = matrix[row_start][col_start]

  for row in matrix[row_start:row_end+1]:
    for element in row[col_start:col_end+1]:
      if(element != first_element):
        return False
  
  return True

def divied_and_conquer(matrix:list, row_start:int, row_end:int, col_start:int, col_end:int):
  global white_count
  global blue_count
  n = row_end - row_start

  if(n == 0 and matrix[row_start][col_start] == 0):
    white_count += 1
    return
  if(n == 0 and matrix[row_start][col_start] == 1):
    blue_count += 1
    return  

  if(is_same(matrix, row_start, row_end, col_start, col_end)):
    if(matrix[row_start][col_start] == 0):
      white_count += 1
      return
    if(matrix[row_start][col_start] == 1):
      blue_count += 1
      return  
  
  row_mid = (row_start + row_end) // 2
  col_mid = (col_start + col_end) // 2
  divied_and_conquer(matrix, row_start, row_mid, col_start, col_mid)
  divied_and_conquer(matrix, row_mid + 1, row_end, col_start, col_mid)
  divied_and_conquer(matrix, row_start, row_mid, col_mid + 1, col_end)
  divied_and_conquer(matrix, row_mid + 1, row_end, col_mid + 1, col_end)

  return


n = int(input())

some_matrix = [[0] * n for _ in range(n)]


for i in range(n):
  some_matrix[i] = list(map(int, input().strip().split()))


divied_and_conquer(some_matrix, 0, n - 1, 0, n - 1)

print(white_count)
print(blue_count)