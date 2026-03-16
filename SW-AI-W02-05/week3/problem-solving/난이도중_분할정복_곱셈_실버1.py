# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
"""
* 원래 풀려했던 방법
* ((A^(B-1) % C) * 2) % C

* 문제점
* O(n)을 재귀로 호출해서 recursion limit 런타임 에러가 발생했음

* 개선 방법
* 홀수일때, a^(b-1/2) * a^(b-1/2) * a
* 짝수일때, a^(b/2) * a(b/2)
* 다음과 같이 분할 정복을 해 O(n)에서 O(log n)으로 시간 복잡도를 개선
* 따라서, 재귀 호출의 수도 log n으로 감소

* 내가 왜 이렇게 생각했을까?
* 곱셈이 느린 연산이라 생각해서 곱셈보다 덧셈을 사용할려고 했음 a^(b-1) + a^(b-1) = a^(b)
* 사실 연산자보다 시간 복잡도가 더 중요한데 중요한걸 놓치고 있었음
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