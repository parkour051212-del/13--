#39

def print_odds(n):
    for i in range(0, n + 1):
        if i % 2 == 1:
            print(i)

num = int(input("양수를 입력하세요: "))
print_odds(num)

#40

def print_multiple_of_three(num):
    if num % 3 == 0:
        print(num)

number = int(input("숫자를 입력하세요: "))
print_multiple_of_three(number)

#41

def find_max_min(a, b, c, d):
    numbers = [a, b, c, d]
    return max(numbers), min(numbers)

n1 = int(input("첫 번째 숫자 입력: "))
n2 = int(input("두 번째 숫자 입력: "))
n3 = int(input("세 번째 숫자 입력: "))
n4 = int(input("네 번째 숫자 입력: "))

maximum, minimum = find_max_min(n1, n2, n3, n4)
print("최댓값:", maximum)
print("최솟값:", minimum)

#42

def print_odds_upto(n):
    for i in range(n+1):
        if i % 2 == 1:
            print(i, end=" ")

num = int(input("양수를 입력하세요: "))
print_odds_upto(num)

#43

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("0 이상의 정수를 입력하세요: "))
print(f"{num}! =", factorial(num))

#44

def sum_products_over_30(i, j):
    total = 0
    for x in range(1, i+1):
        for y in range(1, j+1):
            if x * y >= 30:
                total += x * y
    return total

i = int(input("첫 번째 숫자(20 이상): "))
j = int(input("두 번째 숫자(9 이하): "))

print("총 합:", sum_products_over_30(i, j))

#45

def cumulative_sum(lst):
    total = 0
    for value in lst:
        total += value
        print(total, end=" ")

a = [1, 2, 3, 4, 5]
cumulative_sum(a)