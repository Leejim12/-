# 직사각형 넓이
def solution(dots):
    x1 = dots[0][0]
    for i in range (0,4):
        if dots[i][0] != x1:
            x2 = dots[i][0]
            break
    y1 = dots[0][1]
    for i in range(0,4):
        if dots[i][1] != y1:
            y2 = dots[i][1]
            break
    answer = abs((y2-y1)*(x2-x1))
    return answer