# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
split_minus = input().split('-')

results = []

for nums in split_minus:
  if('+' in nums):
    nums_list = list(map(int, nums.split('+')))
    results.append(sum(nums_list))
  else:
    results.append(int(nums))

result = results[0]

for i in range(1,len(results)):
  result -= results[i]

print(result)