# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
from enum import Enum
import sys
input = sys.stdin.readline

class Direction(Enum):
  RIGHT = 1
  DOWN = 2
  LEFT = 3
  UP = 4

def main():
  status = Direction.RIGHT
  snake_info = []
  head = [0, 0]
  time_index = 0

  #todo 0. 입력 받아서 저장
  #todo 1. n x n 크기의 2차원 배열을 0으로 초기화
  board_size = int(input())
  apple_count = int(input())
  apple_info = []
  for _ in range(apple_count):
    apple_info.append(tuple(map(int, input().split())))

  commands_count = int(input())
  commands = [0] * 10001
  for _ in range(commands_count):
    time, command = input().split()
    commands[int(time)] = command

  board = [[0 for _ in range(board_size)] for _ in range(board_size)]

  #todo 2. 사과가 있는 곳을 1로 변경
  for row, col in apple_info:
    board[row - 1][col - 1] = 1
  #todo 3. 머리를 1칸 이동, time_idx +1
  if(status == Direction.RIGHT):
    head[1] += 1
    time_index += 1
    snake_info.append(head)
  if(status == Direction.DOWN):
    head[0] += 1
    time_index += 1
    snake_info.append(head)
  if(status == Direction.LEFT):
    head[1] -= 1
    time_index += 1
    snake_info.append(head)
  if(status == Direction.UP):
    head[0] -= 1
    time_index += 1
    snake_info.append(head)
  #todo 4. 머리가 보드를 벗어났는지 체크: 머리의 이동 좌표가 == n or == -1이면 게임 종료
  if(head[0] == -1 or head[0] == board_size or head[1] == -1 or head[1] == board_size):
    print(time_index)
    return
  #todo 5. 머리가 자신과 부딪쳤는지 체크: 큐에 갈려는 좌표가 있으면 게임 종료
  if(head in snake_info):
    print(time_index)
    return
  #todo 6. 머리의 위치에 사과가 있는지 체크
  #todo   사과가 있으면, 꼬리 이동 x
  #todo   사과가 없으면, 꼬리 이동: 큐에 있는 이동 정보 deque
  row, col = head
  if(board[row - 1][col - 1] == 1):
    snake_info.pop(0)
  #todo 7. spin_command[time_idx]에 명령이 있는지 체크, 있으면 방향 전환
  command = commands[time_index]
  if(command):
    if(command == 'D'):
      status += 1
      if(status == 5):
        status = 1
    if(command == 'L'):
      status -= 1
      if(status == 0):
        status = 4

  #todo
  #todo
  #todo

main()