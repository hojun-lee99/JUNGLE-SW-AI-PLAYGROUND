# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

N = int(input().strip())
count_available_case = 0

def nqueens(row, col):
  global count_available_case
  if(row == N):
    count_available_case += 1
    return
  
  for current_col in range(N):
    if(is_available(col, row, current_col)):
      col.append(current_col)
      nqueens(row+1, col)
      col.pop()
  return
  
def is_available(col, current_row, current_col):
  # col에 들어있는 queens를 하나씩 꺼내서
  for row in range(len(col)):
    # 세로 비교랑, 대각선 비교
    # 세로 비교: col[i]랑 currnet_col이 같은지 비교
    # 대각선 비교는: current_row - row == current_col - col[row]   
    if(current_col == col[row] or abs(current_col - col[row]) == current_row - row):
      return False
  return True

nqueens(0, [])

print(count_available_case)