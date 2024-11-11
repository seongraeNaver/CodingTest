def solution(my_string, is_suffix):
    answer = []
    result = 0
    
    for i in range(len(my_string)):
        answer.append(my_string[i::])
    for i in answer:
        if i == is_suffix:
            result = 1
    return result 