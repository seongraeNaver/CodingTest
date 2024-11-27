def solution(numbers):
    max_product = float('-inf')  # 초기값을 음의 무한대로 설정 (가장 작은 값)
    n = len(numbers)
    
    # 모든 가능한 두 숫자 쌍을 탐색
    for i in range(n):
        for j in range(i + 1, n):  # i와 j가 같은 쌍은 제외
            product = numbers[i] * numbers[j]
            if product > max_product:
                max_product = product
                
    return max_product
