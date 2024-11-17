def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i = i+1
        elif len(stk) != 0:
            if stk[-1] == arr[i]:
                stk = stk[:len(stk)-1]
                i = i+1
            elif stk[-1] != arr[i]:
                stk.append(arr[i])
                i = i+ 1
        
    if stk:
        return stk
    else:
        return [-1]
    
    
    