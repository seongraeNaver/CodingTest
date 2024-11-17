
def solution(strArr):
    char = []
    count = [0] * (len(strArr) + 1)
    s = 0
    for i in strArr:
        s = len(i)
        count[s] += 1
    
    return max(count)
