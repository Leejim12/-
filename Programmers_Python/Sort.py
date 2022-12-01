def solution(my_string, num1, num2):
    answer = ''
    temp = list(my_string)
    a = temp[num1]
    temp[num1] = temp[num2]
    temp[num2] = a
    for i in temp:
        answer = answer + i
    return answer

s = "hello"
solution(s,1,2)
