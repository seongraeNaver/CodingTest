def solution(my_str, n):
    result = []
    answer = ''
    for idx, value in enumerate(my_str):
        answer += value
        if len(answer) == n or idx == len(my_str) -1:
            result.append(answer)
            answer = ''
            
    return result