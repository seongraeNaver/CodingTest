def solution(my_string):
    answer = []
    word = ''
    
    for char in my_string:
        if char == ' ':
            if word:
                answer.append(word)
                word = ''
        else:
            word += char
            
    if word:
        answer.append(word)
        
    return answer