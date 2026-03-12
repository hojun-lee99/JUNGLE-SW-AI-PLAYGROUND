# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

n = [int(input()) for _ in range(9)]
max_num = max(n)
print(max_num)
print(n.index(max_num)+1)

