def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x = input("Enter the first variable (x): ")
y = input("Enter the second variable (y): ")
x, y = swap_with_temp(x, y)
print(f"After swapping: x = {x}, y = {y}")