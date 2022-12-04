def solution(lines):
    memo = []
    for i in range(lines[0][0],lines[0][1]):
        memo.append(i)
    for i in range(lines[1][0],lines[1][1]):
        memo.append(i)
    for i in range(lines[2][0],lines[2][1]):
        memo.append(i)
    memo.sort()
    print(memo)
    tp = []
    answer = 0
    for i in range(0,len(memo)-1):
        if memo[i] in memo[i+1:len(memo)] and memo[i] not in tp:
           tp.append(memo[i])
    print(tp)
    for i in tp:
        answer = answer + 1
    return answer

lines = [[0, 5], [3, 9], [1, 10]]
print(solution(lines))