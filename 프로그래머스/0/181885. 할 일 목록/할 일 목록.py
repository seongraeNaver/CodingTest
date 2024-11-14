def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if not finished[i] :
            answer.append(todo_list[i])
        else:
            pass
    return answer

