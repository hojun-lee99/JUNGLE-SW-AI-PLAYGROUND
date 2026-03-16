# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
"""
((A^(B-1) % C) * 2 * 10) % C
"""
import sys
input = sys.stdin.readline

def divide_and_conquer(a, b, c):
  if(b == 0):
    return 1 % c
  
  value = divide_and_conquer(a, b//2, c)
  
  if(b % 2  == 1):
    return (value * value * a) % c
    
  return (value * value) % c



nums = list(map(int, input().split()))

print(divide_and_conquer(nums[0], nums[1], nums[2]))