numbers = [1,2,3,4,5,6,7,8]
strings = ["hello", "world"]

anys = [1, "hello", True,[1,2,3,4]]

print( numbers[0])
print(strings[0])

print(anys[3][3])

scores = [84,65,79,91,66,75,56,36,78,97,]

print(scores[3:])
print(scores[1:4])
print(scores[:3])

#평균을 구하고 싶을 때
sum = 0
for i in scores:
    sum = sum + i
average = sum /len(scores)

print("학생들의 점수 총합", sum)
print("학생들의 평균 점수", average)