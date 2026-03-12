# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
  p_list = []

  r, s = input().strip().split(' ')

  for i in s:
    p_list.append(i*int(r))

  print(''.join(p_list))