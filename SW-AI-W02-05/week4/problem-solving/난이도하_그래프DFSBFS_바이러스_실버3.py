# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606
import sys
input = sys.stdin.readline

num_computer = int(input())
num = int(input())

network = {}
for i in range(1, num_computer+1):
  network[i] = []

for j in range(num):
  n, m = list(map(int, input().split()))
  network[n].append(m)
  network[m].append(n)

visited = []
queue = []
queue.append(1)
visited.append(1)
num_virus_computer = 0

while(queue):
  current = queue.pop(0)
  for node in network[current]:
    if node not in visited:
      num_virus_computer += 1
      queue.append(node)
      visited.append(node)

print(num_virus_computer)