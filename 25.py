python
num = int(input())

binary = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
