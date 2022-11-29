def solution(sides):
    t = sorted(sides)
    if t[0]+t[1]>t[2]:
        answer = 1
    else:
        answer = 2
    return answer