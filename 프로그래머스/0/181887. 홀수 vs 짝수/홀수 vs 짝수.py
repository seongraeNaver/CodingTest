def solution(num_list):
    answer = 0
    evensum = 0
    oddsum = 0
    for i in range(len(num_list)):
        if i%2 == 0:
            evensum += num_list[i]
        else:
            oddsum += num_list[i]
            
    if evensum >= oddsum:
        return evensum
    else:
        return oddsum