# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

"""
메모리 초과! 출력 결과를 저장하고 있어서 발생하는 문제
"""
# def hanoi(n, source, target, auxiliary, result_list):
#   if (n == 1):
#     result_list.append(f"{source} {target}")
#     return 1
  
  
#   return hanoi(n-1, source, auxiliary, target, result_list) + hanoi(1, source, target, auxiliary, result_list) + hanoi(n-1, auxiliary, target, source, result_list)

# def main():
#   result_list = list()

#   print(hanoi(size, "1", "3", "2", result_list))

#   if (size < 21):
#     for i in result_list:
#       print(i)


import sys
input = sys.stdin.readline

def hanoi_small_num(n, source, target, auxiliary, result_list):
  if (n == 1):
    result_list.append(f"{source} {target}")
    return 1
    
  return hanoi_small_num(n-1, source, auxiliary, target, result_list) + hanoi_small_num(1, source, target, auxiliary, result_list) + hanoi_small_num(n-1, auxiliary, target, source, result_list)

def hanoi_big_num(n, source, target, auxiliary):
  if (n == 1):
    return 1
    
  return hanoi_big_num(n-1, source, auxiliary, target) * 2 + 1


def main():
  size = int(input())

  if(size <= 20):
    result_list = []
    print(hanoi_small_num(size, "1", "3", "2", result_list))
    for i in result_list :
      print(i)
  else:
    print(hanoi_big_num(size, "1", "3", "2"))

main()

s = str()
s = s + "!"
s.join()
lst = list()