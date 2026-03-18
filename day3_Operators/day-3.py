# 1. Arithmetic Operators (Math)
x = 10
y = 3

print(f"Addition: {x + y}")        # 13
print(f"Subtraction: {x - y}")     # 7
print(f"Multiplication: {x * y}")  # 30
print(f"Division (Float): {x / y}") # 3.333...
print(f"Floor Division: {x // y}") # 3 (removes decimals)
print(f"Modulus: {x % y}")         # 1 (remainder)
print(f"Exponent: {x ** y}")       # 1000 (10 to the power of 3)

# 2. Comparison Operators (Returns True/False)
a = 15
b = 20

print(f"Is a equal to b? {a == b}")      # False
print(f"Is a not equal to b? {a != b}")  # True
print(f"Is a greater than b? {a > b}")   # False

# 3. Assignment Operators (Update values)
score = 100
score += 10    # Same as: score = score + 10
print(f"Updated Score: {score}") # 110

# 4. Logical Operators (Combine conditions)
is_admin = True
has_permission = False

# Returns True only if BOTH are True
print(f"Can access? {is_admin and has_permission}") # False

# Returns True if at least ONE is True
print(f"Can view? {is_admin or has_permission}")   # True
