# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372
import sys
input = sys.stdin.readline
min_num = 0

def dfs(graph, start, visited=None):
  global min_num

  if not visited: visited = []
  if len(visited) == len(graph): return


  visited.append(start)

  for node in graph[start]:
    if node not in visited:
      min_num += 1
      dfs(graph, node, visited)

t = int(input())

for i in range(t):
  n, m = input().split()
  graph = {}

  for i in range(1, int(n) + 1):
    graph[i] = []

  for i in range(int(m)):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

  dfs(graph, 1)
  print(min_num)

  min_num = 0
