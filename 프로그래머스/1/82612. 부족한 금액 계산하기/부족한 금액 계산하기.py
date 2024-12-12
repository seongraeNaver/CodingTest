def solution(price, money, count):
    sum = 0
    result = 0
    for i in range(count):
        sum = sum + price
        result += sum
    print(result)
    
    if result> money:
        return result - money
    else:
        return 0