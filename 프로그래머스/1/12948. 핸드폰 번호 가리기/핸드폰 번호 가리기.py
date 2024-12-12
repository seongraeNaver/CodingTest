def solution(phone_number):
    answer = ''
    result = ''
    index = 0
    for i in phone_number[::-1]:
        if len(answer) >= 4:
            answer += '*'
        else:
            answer += i  
    for i in answer[::-1]:
        result += i
    return result
            