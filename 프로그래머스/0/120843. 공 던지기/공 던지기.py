def solution(numbers, k):
    answer = 0
    while k > 1:
        answer += 2
        answer = answer % len(numbers)
        k = k-1
    return numbers[answer]

