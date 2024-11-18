def solution(rank, attendance):
    eligible = []
    for i in range(len(rank)):
        if attendance[i]:
            eligible.append((rank[i], i))
            
    eligible.sort()
    
    top3 = []
    for j in range(3):
        top3.append(eligible[j][1])
        
    result = 10000*top3[0] + 100*top3[1] + top3[2]
    
    return result