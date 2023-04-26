# 반복문 처리(For Loop)
# for item in list_of_items:
"""
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+"pie")
print("\n")
print(fruits)
"""


# 예제1 - 평균 구하기
student_heights = input("Input a list of student height").split()
num = len(student_heights)
for n in range(0, num):
    student_heights[n] = int(student_heights[n])
total = sum(student_heights)
print("점수 총합: " + str(total))
# print에서는 같은 자료형으로 통일해줘야 함[아니면 TypeError 발생]
avg = round(total / num)
print("평균: " + str(avg))


# 예제2 - 가장 큰 값 구하기
student_scores = input("Input a list of student score").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

if len(student_scores) == 0:
    print("아무것도 입력X")
    quit()
high = student_scores[0]
for score in student_scores:
    if high < score:
        high = score
print("가장 높은 값은: {}".format(high))
