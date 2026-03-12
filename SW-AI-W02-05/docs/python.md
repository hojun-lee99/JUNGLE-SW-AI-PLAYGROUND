# 파이썬 기본 문법

## 입력

### N값만큼 N줄에 1개씩 입력 받기

```python
N = int(input())
M = [int(input()) for _ in range(N)]
```

## 반복문

`for i in range(n)`

## 리스트 순회 방법

다음과 같은 리스트가 있다고 한다.

`fruits = ['사과', '바나나', '포도']`

1. `for`문 사용

```python
for fruit in fruits:
  print(fruit)
```

2. `enumerate()` 함수 활용

`enumerate()`함수는 튜플을 열거 객체로 변환하는 함수이다.

```python
x = ('appale', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

# 실행결과
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

```python
  for index, fruit in enumerate(fruits):
  print(f"{index}번째 과일: {fruit}")
```

3. 리스트 컴프리헨션 (List Comprehension)

기존 리스트를 순회해서 새로운 리스트를 만들때 쓰는 방법

```python
juice_list = [fruit + '주스' for fruit in fruits]
print(juice_list)

# 실행 결과
# ['사과주스', '바나나주스', '포도주스']
```

## 딕셔너리 순회 방법
```python
for key in dic.keys():
```
```python
for value in dic.values():
```
```python
for key, value in dic.items():
```

## 다차원 배열 선언방법

컴프리헨션 방식

`matrix = [[0 for _ in range(n)] for _ in range(n)]`

`*` 기호를 사용해 배열을 선언할시 같은 주소를 공유해서 배열이 만들어 지므로
1번째 열과 2번째 열이 같은 메모리 공간을 차지하게 되므로 사용하지 않는다!