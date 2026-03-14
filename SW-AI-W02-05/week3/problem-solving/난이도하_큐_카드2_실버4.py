# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

def main():
  n = int(input())

  if(n == 1):
    print(1)
    return

  dequeue = deque(i for i in range(1, n, 2))

  if(n % 2 == 1):
    dequeue.append(dequeue.popleft())

  while(len(dequeue) != 1):
    dequeue.popleft()
    dequeue.append(dequeue.popleft())

  print(dequeue.popleft() + 1)

main()


#! 마지막 출력때 + 1
"""
  1, 2, 3, 4, 5
  1 <- 3, 4, 5, 2
  3 <- 5, 2, 4
  5 <- 4, 2
  4 <- 2

  1, 2, 3, 4, 5, 6, 
  1 <- 3, 4, 5, 6, 2
  3 <- 5, 6, 2, 4
  5 <- 2, 4, 6,
  2 <- 6, 4
  6 <- 4

  1, 2, 3, 4, 5, 6, 7
  1 <- 3, 4, 5, 6, 7, 2
  3 <- 5, 6, 7, 2, 4
  5 <- 7, 2, 4, 6,
  7 <- 4, 6, 2
  4 <- 2, 6
  2 <- 6

  1, 2, 3, 4, 5, 6, 7, 8
  1 <- 3, 4, 5, 6, 7, 8, 2
  3 <- 5, 6, 7, 8, 2, 4
  5 <- 7, 8, 2, 4, 6,
  7 <- 2, 4, 6, 8
  2 <- 6, 8, 4
  6 <- 4, 8
  4 <- 8

  1, 2, 3, 4, 5, 6, 7, 8, 9
  9 <- 4, 6, 8, 2
  4 <- 8, 2, 6
  8 <- 6, 2
  6 <- 2
"""
