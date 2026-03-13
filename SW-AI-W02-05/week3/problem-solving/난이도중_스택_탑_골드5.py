# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493


"""
! 시간초과!!!
"""
# import sys
# input = sys.stdin.readline

# num = int(input().strip())

# tower_list = list(map(int, input().strip().split()))

# index_list = []

# for _ in range(len(tower_list)):
#   current_tower = tower_list.pop()
  
#   for i in range(len(tower_list)):
#     reverse_i = len(tower_list) - i - 1
#     if(tower_list[reverse_i] >= current_tower):
#       index_list.insert(0, reverse_i + 1)
#       break
#     if(i == len(tower_list) - 1):
#       index_list.insert(0 ,0)

# index_list.insert(0, 0)

# index_str = ' '.join(list(map(str, index_list)))
# print(index_str)


import sys
input = sys.stdin.readline

n = int(input().strip())
tower_list = list(map(int, input().strip().split()))

answer = []
stack = [] # (인덱스, 탑의 높이) 형태의 튜플을 저장할 스택

for i in range(n):
  current_tower = tower_list[i]
    
    # 1. 스택이 비어있지 않고, 스택의 제일 위(top)에 있는 탑의 높이가 현재 탑보다 낮다면
    # 그 탑은 앞으로 레이저를 받을 일이 없으므로 pop()으로 제거합니다.
  while(stack):
    if(stack[-1][1] < current_tower):
      stack.pop()
    else:
      answer.append(stack[-1][0] + 1)
      break
    
          
  # 2. 스택이 비어있다면, 현재 탑의 레이저를 수신할 탑이 왼쪽에 없다는 뜻입니다.
  if(not stack):
    answer.append(0)
      
  # 3. 현재 탑을 스택에 넣습니다. (다음 탑들의 레이저를 수신할 수도 있으므로)
  stack.append((i, current_tower))

# 결과 출력
print(' '.join(map(str, answer)))