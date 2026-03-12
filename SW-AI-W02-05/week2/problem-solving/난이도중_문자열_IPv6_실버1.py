# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

"""
1. 입력을 받고
2. ':' 기준으로 분리해 리스트에 담기
3. 리스트의 각가 요소의 길이가 4미만일때 앞쪽에 0 채워주기

추가적으로 구현해줘야할 기능
  리스트의 크기를 8개에 맞춰서 빈 문자열을 올바른 위치에 넣어줘야함
1. 빈문자열이 들어가있는 곳을 찾고
2. 해당 인덱스에 8 - len(list_data) 만큼 '' 넣어주기
"""

import sys
input = sys.stdin.readline

input_data = input().strip()
data_to_list = input_data.split(':')
len_data = len(data_to_list)


if('' in data_to_list):
  index = data_to_list.index('')

  if(len_data > 8):
    data_to_list.remove('')
  else:
    for i in range(8 - len_data):
      data_to_list.insert(index, '0000')


ip_list = []

for ip in data_to_list:
  if(len(ip) < 4):
    zero_string = "0" * (4 - len(ip))

    ip_list.append(zero_string + ip)
  else:
    ip_list.append(ip)
    

print(':'.join(ip_list))