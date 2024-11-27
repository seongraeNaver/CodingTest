def solution(numbers):
    max_result = -1e9
    n = len(numbers)
    
    for i in range(n):
        for j in range(i+1, n):
            result = numbers[i] * numbers[j]
            if max_result < result:
                max_result = result
                
    return max_result
    
