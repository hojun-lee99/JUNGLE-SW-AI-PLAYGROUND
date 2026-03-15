# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline    

# def switch_command(command: list, string_stack: list, saved_stack: list):
#   if(command[0] == 'L'):
#     if(len(string_stack) == 0):
#       return
#     saved_stack.append(string_stack.pop())
#     return
#   if(command[0] == 'D'):
#     if(len(saved_stack) == 0):
#       return
#     string_stack.append(saved_stack.pop())
#     return
#   if(command[0] == 'B'):
#     if(len(string_stack) == 0):
#       return
#     string_stack.pop()
#     return
#   if(command[0] == 'P'):
#     string_stack.append(command[1])
#     return

# string_stack = list(input().strip())
# saved_stack = []

# n = int(input().strip())
# commands = []
# for _ in range(n):
#   commands.append(input().strip().split())

# for command in commands:
#   switch_command(command, string_stack, saved_stack)

# while(saved_stack):
#   string_stack.append(saved_stack.pop())

# print(''.join(string_stack))


class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
    pass

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.cursor = None
    self.tail = None

  def append(self, node: Node):
    if(not self.head):
      self.head = node
      self.cursor = node
      self.tail = node
      return
    
    self.tail.next = node
    node.prev = self.tail
    self.cursor = node
    self.tail = node
    pass

  def go_prev(self):
    if(self.cursor == None):
      return
    self.cursor = self.cursor.prev
    pass

  def go_next(self):
    if(self.cursor == self.tail):
      return
    if(self.cursor == None):
      self.cursor = self.head
      return
    self.cursor = self.cursor.next
    pass

  def deleted_by_cursor(self):
    # 맨 앞에 있는 경우
    if(not self.cursor):
      return
    # 요소가 하나만 남았을때
    if(not self.cursor.prev and not self.cursor.next):
      self.head = None
      self.cursor = None
      self.tail = None
      return
    # head에 있는 경우
    if(not self.cursor.prev):
      self.cursor.next.prev = None
      self.head = self.cursor.next
      self.cursor = None
      return
    # 맨 뒤에 있는 경우
    if(not self.cursor.next):
      self.cursor.prev.next = None
      self.tail = self.cursor.prev
      self.cursor = self.tail
      return
    # 노드 사이에 있는 경우
    self.cursor.next.prev = self.cursor.prev
    self.cursor.prev.next = self.cursor.next
    self.cursor = self.cursor.prev
    return


  def insert_by_cursor(self, node: Node):
    # 비어있을때
    if(not self.head and not self.tail and not self.cursor):
      self.head = node
      self.tail = node
      self.cursor = node
      return
    # 커서가 맨 앞 일때
    if(not self.cursor):
      self.cursor = node
      self.cursor.next = self.head
      self.head.prev = self.cursor
      self.head = self.cursor
      return
    #커서가 맨 뒤 일때
    if(self.cursor.next == None):
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
      self.cursor = node
      return
    
    node.next = self.cursor.next
    node.prev = self.cursor
    self.cursor.next = node
    node.next.prev = node
    self.cursor = node
    pass

  def print_all_data(self):
    self.cursor = self.head
    while(self.cursor):
      print(self.cursor.data, end='')
      self.cursor = self.cursor.next



def switch_command(command: list, string_list: DoubleLinkedList):
  if(command[0] == 'L'):
    string_list.go_prev()
    return
  if(command[0] == 'D'):
    string_list.go_next()
    return
  if(command[0] == 'B'):
    string_list.deleted_by_cursor()
    return
  if(command[0] == 'P'):
    string_list.insert_by_cursor(Node(command[1]))
    return
  
string_list = DoubleLinkedList()
string_stack = list(input().strip())

for data in string_stack:
  string_list.append(Node(data))

n = int(input().strip())
commands = []
for _ in range(n):
  commands.append(input().strip().split())

for command in commands:
  switch_command(command, string_list)

string_list.print_all_data()