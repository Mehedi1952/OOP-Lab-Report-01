import cmath
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
roots = solve_quadratic(a, b, c)
print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")