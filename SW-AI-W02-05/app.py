# def nsum(n):
#   sum = 0
#   for i in range(1,n+1):
#     sum += n
#   return sum

# def nsum_2(n):
#   return sum(list(range(n+1)))

# def nsum_recursion(n):
#   if(n == 1):
#     return 1
#   return n + nsum_recursion(n-1)

# # tail recursion
# # 일반 recursion 보다 실행시간이 절반으로 줄어듦
# def nsum_iter(n, total):
#   if n == 0:
#     return total
#   else:
#     return nsum_iter(n-1, total+n)

# def sum(n):
#   return nsum_iter(5, 0)

# # Exponentiation 거듭제곱
# def exp_recursion(b, n):
#   if n == 0:
#     return 1
#   return b * exp_recursion(b, n-1)

# print(exp_recursion(2, 10))

# # 짝수일때 nlogn으로 개선한 방법
# def exp_fast(b, n):
#   if n == 0:
#     return 1
#   if is_even(n):
#     return exp_recursion(b, n/2) * exp_recursion(b, n/2)
#   else:
#     exp_recursion(b, n-1)

# # 피보나치
# def Fib(n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return 1
#   return Fib(n-1) + Fib(n-2)

# def Fib_tail_recursion():
#   return

# # 거스름돈 구하는 법
# def count_change(n, coins):
#   if n == 0:
#     return 1
#   if n < 0 or len(coins) == 0:
#     return 0
#   return count_change(n, coins[1:]) + count_change(n - coins[0], coins)

# # 하노이 탑
# # def hanoi(first, sceond, third, rings[]):
  

# str1 = "hello"
# str2 = "world"
# newstr = str1.__add__(str2)

def letterNumCombination(str):
  letters_list = {2 : ['a','b','c'],
                  3 : ['d','e','f'],
                  4 : ['g','h','i'],
                  5 : ['j','k','l'],
                  6 : ['m','n','o'],
                  7 : ['p','q','r','s'],
                  8 : ['t','u','v'],
                  9 : ['w','x','y','z']}
  digits_list = list(map(int, str))
  combinations_result = []

  def backtrack(index, combination):

    if(index >= len(digits_list)):
      combinations_result.append(combination.copy())
      return
    
    num = digits_list[index]

    for i in range(len(letters_list[num])):
      combination.append(letters_list[num][i])
      backtrack(index+1, combination)
      combination.pop()

  backtrack(0, [])

  
  return combinations_result

print(letterNumCombination("234"))