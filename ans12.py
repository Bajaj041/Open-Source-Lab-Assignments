def my_filter(func, lst):
    return [x for x in lst if func(x)]

nums = [1, 2, 3, 4, 5, 6]
evens = my_filter(lambda x: x % 2 == 0, nums)
print(evens) 
