def triplet(n):
    result = []
    for a in range(n):
        for b in range(a, n):
            c = a + b
            if c < n:
                result.append((a, b, c))
    return result

print(triplet(10))
