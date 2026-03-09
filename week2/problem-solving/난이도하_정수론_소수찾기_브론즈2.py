# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline

def is_prime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  if(num % 2 == 0):
    return False
  for i in range(3, int(num**0.5) + 1, 2):
    if (num % i == 0):
      return False
  return True

n = input()
n_list = list(map(int, input().split()))
prime_list = list()

for i in n_list:
  if(is_prime(int(i))):
    prime_list.append(i)

print(len(prime_list))