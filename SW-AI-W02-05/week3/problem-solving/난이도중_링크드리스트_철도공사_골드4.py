# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
"""
* BN i j : 고유 번호 i를 가진 역의 다음 역의 고유 번호를 출력하고, 그 사이에 고유 번호 j인 역을 설립한다.
* BP i j : 고유 번호 i를 가진 역의 이전 역의 고유 번호를 출력하고, 그 사이에 고유 번호 j인 역을 설립한다.
* CN i : 고유 번호 i를 가진 역의 다음 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
* CP i : 고유 번호 i를 가진 역의 이전 역을 폐쇄하고 그 역의 고유 번호를 출력한다.
"""

import sys
input = sys.stdin.readline

class Node():
  def __init__(self, unique_num):
    self.unique_num: int = unique_num
    self.next: Node = None
    self.prev: Node = None

class SubwayLine2():
  def __init__(self):
    self.head = None
    # self.tail = None
  
  def _print_unique_num(self, node: Node):
    print(node.unique_num)
    pass

  def _get_find_node(self, unique_num: int):
    next_node = self.head
    
    while(next_node.unique_num != unique_num):
      next_node = next_node.next

    return next_node
  
  def _insert_between(self, first_node: Node, second_node: Node, insert_node: Node):
    first_node.next = insert_node
    insert_node.next = second_node
    second_node.prev = insert_node
    insert_node.prev = first_node

  def _delete_node(self, delete_node: Node):
    delete_node.next.prev = delete_node.prev
    delete_node.prev.next = delete_node.next

  def append(self, unique_num: int):
    append_node = Node(unique_num)
    
    if(self.head == None):
      self.head = append_node
      self.head.next = self.head
      self.head.prev = self.head
      return
        
    self._insert_between(self.head.prev, self.head, append_node)

  def insert_next(self, find_unique_num: int, insert_unique_num: int):
    insert_node = Node(insert_unique_num)
    
    if(self.head.unique_num == find_unique_num):
      self._print_unique_num(self.head.next)
      self._insert_between(self.head, self.head, insert_node)

    find_node = self._get_find_node(find_unique_num)
    next_node = find_node.next
    
    self._print_unique_num(next_node)
    self._insert_between(find_node, next_node, insert_node)

  
  def insert_prev(self, find_unique_num: int, insert_unique_num: int):
    insert_node = Node(insert_unique_num)

    if(self.head.unique_num == find_unique_num):
      self._print_unique_num(self.head.prev)
      self._insert_between(self.head, self.head, insert_node)
    
    find_node = self._get_find_node(find_unique_num)
    prev_node = find_node.prev

    self._print_unique_num(prev_node)
    self._insert_between(prev_node, find_node, insert_node)

  def delete_next(self, find_unique_num: int):
    find_node = self._get_find_node(find_unique_num)
    next_node = find_node.next

    self._print_unique_num(next_node)
    self._delete_node(next_node)

  def delete_prev(self, find_unique_num: int):
    find_node = self._get_find_node(find_unique_num)
    prev_node = find_node.prev

    self._print_unique_num(prev_node)
    self._delete_node(prev_node)

def exec_command(command, subway: SubwayLine2):
  if(command[0] == "BN"):
    find_unique_num = int(command[1])
    insert_unique_num = int(command[2])
    subway.insert_next(find_unique_num, insert_unique_num)
  if(command[0] == "BP"):
    find_unique_num = int(command[1])
    insert_unique_num = int(command[2])
    subway.insert_prev(find_unique_num, insert_unique_num)
  if(command[0] == "CN"):
    find_unique_num = int(command[1])
    subway.delete_next(find_unique_num)
  if(command[0] == "CP"):
    find_unique_num = int(command[1])
    subway.delete_prev(find_unique_num)

def main():
  n, m = list(map(int, input().strip().split()))
  append_list = list(map(int, input().strip().split()))

  subway_line2 = SubwayLine2()

  for i in range(n):
    subway_line2.append(append_list[i])
  
  for i in range(m):
    command = input().strip().split()
    exec_command(command, subway_line2)


main()