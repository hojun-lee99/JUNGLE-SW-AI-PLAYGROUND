# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys
input = sys.stdin.readline

def binary_search(n, list):
  left = 0
  right = len(list) - 1

  while(left < right):
    mid = (left + right) // 2
    if(n == list[mid]):
      return True
    if(n < list[mid]):
      right = mid - 1
    if(n > list[mid]):
      left = mid + 1

  if(n == list[left] and n == list[right]):
    return True
  
  return False

n = int(input().strip())

a_list = list(map(int, input().strip().split()))
m = int(input().strip())
m_list = list(map(int, input().strip().split()))

a_list.sort()

for i in range(len(m_list)):  
  if(binary_search(m_list[i], a_list)):
    print(1)
  else:
    print(0)