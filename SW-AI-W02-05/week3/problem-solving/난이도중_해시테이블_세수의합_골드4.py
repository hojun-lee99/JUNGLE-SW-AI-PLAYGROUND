# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

# def combinations(nums_list):
#   k = 3
#   result = set()

#   def backtrack(current_combination):
#     if(len(current_combination) == k):
#       current_sum = 0
#       for element in current_combination:
#         current_sum += element
#       if(current_sum not in result):
#         result.add(current_sum)
#       return
    
#     for num in nums_list:
#       current_combination.append(num)
#       backtrack(current_combination)
#       current_combination.pop()
  
#   backtrack([])
#   return result

s = set()
nums_list = []

n = int(input())

for _ in range(n):
  num = int(input())
  s.add(num)
  nums_list.append(num)

cwr_list = []
cwr_sum_set = set()
#TODO a+b를 구하고
for cwr in combinations_with_replacement(nums_list, 2):
  cwr_list.append(cwr)
  sum_cwr = sum(cwr)
  cwr_sum_set.add(sum_cwr)

#TODO d-c를 구해서 비교
max_num = 0
for x, y in cwr_list:
  subbed_val = abs(x - y)
  if(subbed_val in cwr_sum_set):
    max_elem = max(x, y)
    if(max_num < max_elem):
      max_num = max_elem

#TODO 가장 큰값을 출력
print(max_num)