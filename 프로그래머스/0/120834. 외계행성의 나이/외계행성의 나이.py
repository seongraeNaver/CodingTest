def solution(age):
    alpabet = 'abcdefghijklmnopqrstuvwxyz'
    ages = [int(age) for age in str(age)]
    s = ''
    for i in ages:
        s += alpabet[i]
    
    return s