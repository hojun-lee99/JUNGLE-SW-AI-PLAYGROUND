# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

n = int(input())

for _ in range(n):
  size_over_avg_students = 0
  list_int = [int(x) for x in input().split()]
  size_students = list_int.pop(0)
  avg = sum(list_int) / size_students
  size_over_avg_students = sum(i > avg for i in list_int)
  
  ratio_over_avg = size_over_avg_students / size_students * 100
  print(f'{ratio_over_avg:.3f}%')

