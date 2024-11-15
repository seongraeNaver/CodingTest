def solution(myString, pat):
    count = 0
    for i in range(0, len(myString)- len(pat)+1):
        if myString[i : i+len(pat)] == pat:
            count += 1
    return count 

# def solution(myString, pat):
#     cnt = 0
#     for i in range(0, len(myString) - len(pat) + 1):
#         if myString[i : i+len(pat)] == pat:
#             cnt += 1
#     return cnt
