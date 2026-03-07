# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
import sys
input = sys.stdin.readline

s = input().strip()
s_list = []

for char in s:
  dic = {}
  s_list.append(char.upper())

str = ''.join(s_list)

for i, value in enumerate(s_list[:]):
  if not dic.get(value):
    dic[value] = 1
  else:
    dic[value] += 1

max_value = max(dic.values())
max_key = None

for key in dic:
  if dic[key] == max_value:
    if not max_key:
      max_key = key
    else:
      max_key = '?'

print(max_key)