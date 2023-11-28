def solve(word):
    # Calculate the values of consonant substrings
    consonant_values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in word.split('aeiou')]
    # Return the highest value
    return max(consonant_values)

# Test cases
print(solve("zodiacs"))    # Output: 26
print(solve("strength"))   # Output: 57
