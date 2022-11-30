def solution(numbers):
    numbers.sort()
    n1 = numbers[len(numbers)-1]*numbers[len(numbers)-2]
    n2 = numbers[len(numbers)-1]*numbers[0]
    n3 = numbers[1]*numbers[0]
    com = [n1,n2,n3]
    com.sort()
    answer = com[2]
    return answer

e = [1, 2, -3, 4, -5]	
print(solution(e))