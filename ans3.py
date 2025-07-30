def duplicate(int_list):
    seen = set()
    duplicates = set()
    
    for num in int_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
print("Duplicates:", duplicate(numbers))
