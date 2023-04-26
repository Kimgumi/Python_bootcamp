# range 함수 & 반복문
# --> For Loop with Range
for number in range(1, 11, 2):
    print(number)# 1~100사이에 출력
# 짝수 더하기
total = 0
for number in range(1, 101, 2):
    total += number
print(total)

# fizzbuzz
'''
3의 배수면 fizz, 5의 배수면 buzz,
15의 배수면 fizzbuzz
'''
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 5 != 0:
        print("fizz")
    elif num % 3 != 0:
        print("buzz")
    print(num)

# PW Generator
