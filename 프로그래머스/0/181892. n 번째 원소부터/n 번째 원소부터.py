def solution(num_list, n):
    answer = []
    index = 1
    for i in num_list:
        if index >= n:
            answer.append(i)
        index += 1
    return answer