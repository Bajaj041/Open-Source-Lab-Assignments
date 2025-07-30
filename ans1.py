fruits = []
print("Enter 5 different fruits:")

for i in range(5):
    fruit = input(f"Fruit {i+1}: ")
    fruits.append(fruit)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

print("Middle fruits:", fruits[1:4])
