def solution(quiz):
    answer = []
    for q in quiz:
        expression, result = q.split(" = ")
        result = int(result)
        if "+" in expression:
            x, y = map(int, expression.split(" + "))
            if x + y == result:
                answer.append("O")
            else:
                answer.append("X")
        elif "-" in expression:
            x, y = map(int, expression.split(" - "))
            if x - y == result:
                answer.append("O")
            else:
                answer.append("X")
    return answer
