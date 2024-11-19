def solution(order):
    total_cost = 0
    for item in order:
        if "americano" in item or item == "anything":
            total_cost += 4500
        elif "cafelatte" in item:
            total_cost += 5000
    return total_cost