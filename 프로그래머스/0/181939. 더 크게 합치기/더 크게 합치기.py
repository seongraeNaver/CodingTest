def solution(a, b):
    result1 = int(str(a) + str(b))
    result2 = int(str(b) + str(a))
    if result1 > result2 :
        return result1
    elif result1 < result2:
        return result2
    else:
        return result1