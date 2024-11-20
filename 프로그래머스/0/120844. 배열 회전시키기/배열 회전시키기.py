def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:len(numbers)-1]
    elif direction == "left":
        return numbers[1:len(numbers)] + [numbers[0]]