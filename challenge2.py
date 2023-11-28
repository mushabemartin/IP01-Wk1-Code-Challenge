def exactly_two_positive(a, b, c):
    # Count the number of positive numbers using a condition
    positive_count = (a > 0) + (b > 0) + (c > 0)
    # Return True if exactly two numbers are positive, otherwise False
    return positive_count == 2

# Test cases
print(exactly_two_positive(2, 4, -3))   # Output: True
print(exactly_two_positive(-4, 6, 8))   # Output: True
print(exactly_two_positive(4, -6, 9))   # Output: True
print(exactly_two_positive(-4, 6, 0))   # Output: False
print(exactly_two_positive(4, 6, 10))   # Output: False
print(exactly_two_positive(-14, -3, -4))  # Output: False
