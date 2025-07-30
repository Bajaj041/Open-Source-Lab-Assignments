import string

def nearly_equal(a, b):
    letters = string.ascii_lowercase

    if a == b:
        return False

    if abs(len(a) - len(b)) > 1:
        return False

    if len(a) == len(b) + 1:
        for i in range(len(a)):
            if a[:i] + a[i+1:] == b:
                return True

    if len(a) + 1 == len(b):
        for i in range(len(b)):
            if b[:i] + b[i+1:] == a:
                return True

    if len(a) == len(b):
        diff_count = sum(1 for x, y in zip(a, b) if x != y)
        if diff_count == 1:
            return True

        for i in range(len(a) - 1):
            if (a[:i] + a[i+1] + a[i] + a[i+2:]) == b:
                return True

    return False

# Example usage:
print(nearly_equal("cat", "cats"))
print(nearly_equal("cat", "cut"))
print(nearly_equal("cat", "act"))
print(nearly_equal("cat", "at"))
print(nearly_equal("cat", "dog"))
