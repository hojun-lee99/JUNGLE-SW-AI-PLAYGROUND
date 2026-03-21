# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244
import sys
input = sys.stdin.readline

def main():
  num_nodes, num_leaves = list(map(int, input().split()))

  if num_leaves == 2:
    for i in range(num_nodes - 1):
      print(f"{i} {i+1}")
    return

  for i in range(1, num_leaves + 1):
    print(f"{0} {i}")

  for i in range(num_leaves, num_nodes - 1):
    print(f"{i} {i+1}")

main()