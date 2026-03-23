# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173
import sys
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
  board.append(list(map(int, input().split())))


def dfs(r, c):
  is_win = False
  jump_size = board[r][c]

  if(jump_size == 0):
    return False
  next_row = r + jump_size
  next_col = c + jump_size
  if(next_row >= n and next_col >= n):
    return False
  if(next_row < n and board[next_row][c] == -1):
    return True
  if(next_col < n and board[r][next_col] == -1):
    return True
  
  # return을 박아서 밑에 dfs가 안걸리고 그냥 return 됨
  if(next_row < n):
    if(dfs(next_row, c)):
      is_win = True
  if(next_col < n):
    if(dfs(r, next_col)):
      is_win = True

  return is_win

if(dfs(0, 0)):
  print('HaruHaru')
else:
  print('Hing')