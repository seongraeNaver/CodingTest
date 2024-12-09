def solution(n):
    n = str(n)
    n = list(str(n))
    n.sort(reverse = True)
    s = ''
    for i in n:
        s += i
    return int(s)