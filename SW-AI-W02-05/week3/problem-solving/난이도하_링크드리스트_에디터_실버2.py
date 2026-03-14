# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline    

def switch_command(command: list, string_stack: list, saved_stack: list):
  if(command[0] == 'L'):
    if(len(string_stack) == 0):
      return
    saved_stack.append(string_stack.pop())
    return
  if(command[0] == 'D'):
    if(len(saved_stack) == 0):
      return
    string_stack.append(saved_stack.pop())
    return
  if(command[0] == 'B'):
    if(len(string_stack) == 0):
      return
    string_stack.pop()
    return
  if(command[0] == 'P'):
    string_stack.append(command[1])
    return

string_stack = list(input().strip())
saved_stack = []

n = int(input().strip())
commands = []
for _ in range(n):
  commands.append(input().strip().split())

for command in commands:
  switch_command(command, string_stack, saved_stack)

while(saved_stack):
  string_stack.append(saved_stack.pop())

print(''.join(string_stack))