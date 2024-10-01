def get_max_value(n, w, value, weight):
    items = [(value[i] / weight[i], weight[i], value[i]) for i in range(n)]
    
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    
    for ratio, wt, val in items:
        if w == 0:
            break
        if wt <= w:
            w -= wt
            total_value += val
        else:
            total_value += ratio * w
            w = 0
            
    return total_value

# Example
n1, w1 = 3, 50
value1 = [60, 100, 120]
weight1 = [10, 20, 30]
print(f"Output: {get_max_value(n1, w1, value1, weight1):.6f}")

n2, w2 = 2, 50
value2 = [60, 100]
weight2 = [10, 20]
print(f"Output: {get_max_value(n2, w2, value2, weight2):.6f}")