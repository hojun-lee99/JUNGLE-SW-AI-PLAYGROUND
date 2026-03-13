# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

class MyStack:
  def __init__(self):
    self._stack = []
    pass

  def push(self, data):
    self._stack.append(data)

  def pop(self):
    if(len(self._stack) == 0):
      return -1
    return self._stack.pop()
  
  def size(self):
    return len(self._stack)
  
  def empty(self):
    if(len(self._stack) == 0):
      return 1
    return 0
  
  def top(self):
    if(len(self._stack) == 0):
      return -1
    return self._stack[len(self._stack) - 1]
  
def switchInput(input_list, stack):
  if(input_list[0] == 'push'):
    stack.push(input_list[1])
    return
  if(input_list[0] == 'pop'):
    print(stack.pop())
    return
  if(input_list[0] == 'size'):
    print(stack.size())
    return
  if(input_list[0] == 'empty'):
    print(stack.empty())
    return
  if(input_list[0] == 'top'):
    print(stack.top())
    return
  else:
    return


num = int(input())

my_stack = MyStack()
for i in range(num):
  input_list = input().split()
  switchInput(input_list, my_stack)


