def closestInt(array):
    set = sorted(array)
    max_distance = max(set) - min(set)
    actual_distance = max_distance
    for i in range(len(array)-1):
        bound = set[i+1] - set[i]
        if bound < actual_distance:
            actual_distance = bound
    return actual_distance