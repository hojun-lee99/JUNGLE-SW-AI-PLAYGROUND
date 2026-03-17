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

# class Node():
#   def __init__(self, unique_num):
#     self.unique_num: int = unique_num
#     self.next: Node = None
#     self.prev: Node = None

# class SubwayLine2():
#   def __init__(self):
#     self.head = None
#     self.node_list = [None for _ in range(1000001)]
  
#   def _print_unique_num(self, node: Node):
#     print(node.unique_num)

#   def _get_find_node(self, unique_num: int):
#     return self.node_list[unique_num]
  
#   def _insert_between(self, first_node: Node, second_node: Node, insert_node: Node):
#     first_node.next = insert_node
#     insert_node.next = second_node
#     second_node.prev = insert_node
#     insert_node.prev = first_node

#   def _delete_node(self, delete_node: Node):
#     delete_node.next.prev = delete_node.prev
#     delete_node.prev.next = delete_node.next

#   def append(self, unique_num: int):
#     append_node = Node(unique_num)

#     self.node_list[unique_num] = append_node
    
#     if(self.head == None):
#       self.head = append_node
#       self.head.next = self.head
#       self.head.prev = self.head
#       return
        
#     self._insert_between(self.head.prev, self.head, append_node)

#   def insert_next(self, find_unique_num: int, insert_unique_num: int):
#     insert_node = Node(insert_unique_num)
    
#     self.node_list[insert_unique_num] = insert_node

#     find_node = self._get_find_node(find_unique_num)
#     next_node = find_node.next
    
#     self._print_unique_num(next_node)
#     self._insert_between(find_node, next_node, insert_node)

  
#   def insert_prev(self, find_unique_num: int, insert_unique_num: int):
#     insert_node = Node(insert_unique_num)

#     self.node_list[insert_unique_num] = insert_node
    
#     find_node = self._get_find_node(find_unique_num)
#     prev_node = find_node.prev

#     self._print_unique_num(prev_node)
#     self._insert_between(prev_node, find_node, insert_node)

#   def delete_next(self, find_unique_num: int):
#     find_node = self._get_find_node(find_unique_num)
#     next_node = find_node.next

#     self._print_unique_num(next_node)
#     self._delete_node(next_node)

#   def delete_prev(self, find_unique_num: int):
#     find_node = self._get_find_node(find_unique_num)
#     prev_node = find_node.prev

#     self._print_unique_num(prev_node)
#     self._delete_node(prev_node)

# def exec_command(command, subway: SubwayLine2):
#   if(command[0] == "BN"):
#     find_unique_num = int(command[1])
#     insert_unique_num = int(command[2])
#     subway.insert_next(find_unique_num, insert_unique_num)
#     return
#   if(command[0] == "BP"):
#     find_unique_num = int(command[1])
#     insert_unique_num = int(command[2])
#     subway.insert_prev(find_unique_num, insert_unique_num)
#     return
#   if(command[0] == "CN"):
#     find_unique_num = int(command[1])
#     subway.delete_next(find_unique_num)
#     return
#   if(command[0] == "CP"):
#     find_unique_num = int(command[1])
#     subway.delete_prev(find_unique_num)
#     return

# def main():
#   n, m = list(map(int, input().strip().split()))
#   append_list = list(map(int, input().strip().split()))

#   subway_line2 = SubwayLine2()

#   for i in range(n):
#     subway_line2.append(append_list[i])
  
#   for i in range(m):
#     command = input().strip().split()
#     exec_command(command, subway_line2)


# main()




def append_station(unique_num: int):

  return

def insert_next(find_unique_num: int, insert_unique_num: int):

  return

def insert_prev(find_unique_num: int, insert_unique_num: int):

  return

def delete_next(find_unique_num: int):
  
  return

def delete_prev(find_unique_num: int):
  
  return

def exec_command(command):
  pass

def main():
  prev_node_list = [None] * 1000001
  next_node_list = [None] * 1000001
  head = None


  n, m = list(map(int, input().split()))
  append_list = list(map(int, input().split()))

  answer = [0] * m
  answer_index = 0


  for i in range(n):
    if(not head):
      head = append_list[i]
      prev_node_list[append_list[i]] = append_list[i]
      next_node_list[append_list[i]] = append_list[i]
      continue
    
    last_index = prev_node_list[head]

    next_node_list[last_index] = append_list[i]
    prev_node_list[head] = append_list[i]
    prev_node_list[append_list[i]] = last_index
    next_node_list[append_list[i]] = head    
  
  for i in range(m):
    command = input().split()
    if(command[0] == "BN"):
      find_unique_num = int(command[1])
      insert_unique_num = int(command[2])
      next_index = next_node_list[find_unique_num]
      answer[answer_index] = next_index
      answer_index += 1
      next_node_list[find_unique_num] = insert_unique_num
      prev_node_list[next_index] = insert_unique_num
      prev_node_list[insert_unique_num] = find_unique_num
      next_node_list[insert_unique_num] = next_index
      continue
    if(command[0] == "BP"):
      find_unique_num = int(command[1])
      insert_unique_num = int(command[2])
      prev_index = prev_node_list[find_unique_num]
      answer[answer_index] = prev_index
      answer_index += 1
      prev_node_list[find_unique_num] = insert_unique_num
      next_node_list[prev_index] = insert_unique_num
      prev_node_list[insert_unique_num] = prev_index 
      next_node_list[insert_unique_num] = find_unique_num
      continue
    if(command[0] == "CN"):
      find_unique_num = int(command[1])
      next_index = next_node_list[find_unique_num]
      answer[answer_index] = next_index
      answer_index += 1
      next_node_next_index = next_node_list[next_index]
      next_node_list[find_unique_num] = next_node_next_index
      prev_node_list[next_node_next_index] = find_unique_num
      continue
    if(command[0] == "CP"):
      find_unique_num = int(command[1])
      prev_index = prev_node_list[find_unique_num]
      answer[answer_index] = prev_index
      answer_index += 1
      prev_node_prev_index = prev_node_list[prev_index]
      prev_node_list[find_unique_num] = prev_node_prev_index
      next_node_list[prev_node_prev_index] = find_unique_num
      continue    

  sys.stdout.write('\n'.join(map(str, answer)))


main()