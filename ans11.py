def my_map(func, lst):
    return [func(x) for x in lst]

nums = [1, 2, 3, 4]
squared = my_map(lambda x: x**2, nums)
print(squared)
