# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys
input = sys.stdin.readline

def main():
  n = int(input())

  sets = set()

  for _ in range(n):
    chars_list = list(input().strip())

    if(chars_list == list(reversed(chars_list))):
      mid = len(chars_list) // 2
      middle_char = chars_list[mid]
      print(f"{len(chars_list)} {middle_char}")
      return

    if(''.join(list(reversed(chars_list))) in sets):
      mid = len(chars_list) // 2
      middle_char = list(chars_list)[mid]
      print(f"{len(chars_list)} {middle_char}")

    sets.add(''.join(chars_list))


main()