# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
import sys
input = sys.stdin.readline

min_cost = sys.maxsize

def TSP():
  def backtrack(start, current, count, cost):
    global min_cost
    # TODO: base case - n개를 모두 선택했으면 돌아가기
    if (count == N and graph[current][start] != 0):
      min_cost = min(min_cost, cost + graph[current][start])
      return
    # TODO: start부터 N까지 숫자를 하나씩 시도 
    # TODO: 1. 선택, 2. 탐색, 3. 취소
    for i in range(N):
      if( visited[i] == 0 and graph[current][i] != 0):
        visited[i] = 1
        backtrack(start, i, count+1, cost + graph[current][i])
        visited[i] = 0
    

  N = int(input().rstrip())
  graph = [list(map(int, input().split())) for _ in range(N)]
  visited = [0 for _ in range(N)]
  visited[0] = 1

  backtrack(0, 0, 1, 0)
  print(min_cost)

TSP()