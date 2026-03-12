# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

N = int(input().strip())
count_available_case = 0

"""
* 방법1: 일반적인 백트래킹 방식으로 구현
* 시간 초과!!!
* pypy3로 제출시 통과
"""
# def nqueens(row, col):
#   global count_available_case
#   if(row == N):
#     count_available_case += 1
#     return
  
#   for current_col in range(N):
#     if(is_available(col, row, current_col)):
#       col.append(current_col)
#       nqueens(row+1, col)
#       col.pop()
#   return
  
# def is_available(col, current_row, current_col):
#   # col에 들어있는 queens를 하나씩 꺼내서
#   for row in range(len(col)):
#     # 세로 비교랑, 대각선 비교
#     # 세로 비교: col[i]랑 currnet_col이 같은지 비교
#     # 대각선 비교는: current_row - row == current_col - col[row]   
#     if(current_col == col[row] or abs(current_col - col[row]) == current_row - row):
#       return False
#   return True

"""
* 방법2. set을 사용해서 자리 검증 시간 줄이기
* 시간 초과!!!
* 1. set 연산의 숨겨진 비용 (해싱 오버헤드)
* set은 값을 찾거나 추가할 때 $O(1)$이 걸리지만, 내부적으로 해시(Hash) 함수를 계산해야 합니다. N-Queen은 수백만 번 이상 넣고 빼기를 반복해야 하므로 이 해시 계산 시간이 엄청나게 누적됩니다.

* 2. 함수 호출 오버헤드 (is_available)
* 파이썬은 함수를 호출할 때마다 메모리에 새로운 환경을 구성하는 비용(오버헤드)이 꽤 큽니다. 가장 많이 반복되는 for문 안에서 is_available 함수를 매번 호출하고 있으니 엄청난 시간이 소모됩니다.

* pypy3으로 제출 시, 통과
"""
col = set()
positive_diagonal = set()
negative_diagonal = set()

def nqueens(row):
  global count_available_case
  if(row == N):
    count_available_case += 1
    return
  
  for current_col in range(N):
    if( current_col not in col and (row + current_col) not in positive_diagonal and (row - current_col) not in negative_diagonal):
      col.add(current_col)
      positive_diagonal.add(row + current_col)
      negative_diagonal.add(row - current_col)
      nqueens(row+1)
      col.discard(current_col)
      positive_diagonal.discard(row + current_col)
      negative_diagonal.discard(row - current_col)
  return
  
# def is_available( current_row, current_col):
#   if(current_col in col):
#     return False
#   if((current_row + current_col) in positive_diagonal):
#     return False
#   if((current_row - current_col) in negative_diagonal):
#     return False
#   return True

nqueens(0)

print(count_available_case)