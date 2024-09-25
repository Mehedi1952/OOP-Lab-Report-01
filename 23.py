```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())
lcm = (num1 * num2) // gcd(num1, num2)
print(lcm)
```