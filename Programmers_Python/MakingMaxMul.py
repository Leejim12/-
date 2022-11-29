def solution(numbers):
    answer = 0
    t = sorted(numbers)
    answer = t[len(numbers)-1]*t[len(numbers)-2]
    return answer

k = [0, 31, 24, 10, 1, 9]
solution(k)
