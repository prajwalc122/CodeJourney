def second_largest(arr):
    first = second = float('-inf')
    
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    
    return second
