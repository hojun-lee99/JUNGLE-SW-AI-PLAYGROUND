# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
import sys
input = sys.stdin.readline

word = input().strip().upper()

dic = {}

for char in word:
  dic[char] = dic.get(char, 0) + 1

max_value = max(dic.values())
max_key = None

for key in dic:
  if dic[key] == max_value:
    if not max_key:
      max_key = key
    else:
      max_key = '?'

print(max_key)