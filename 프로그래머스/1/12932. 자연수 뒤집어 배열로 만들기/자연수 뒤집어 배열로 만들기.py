def solution(n):
    result = []
    n = str(n)
    for i in n[::-1]:
        result.append(int(i))
    return list(result)