special_chars = [
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\',
    ':', ';', '"', "'",
    '<', '>', ',', '.', '?', '/'
]


def password_validator(password):
    # Initialize counter for special characters
    
    special_char_count = 0
    lower_count=0
    upper_count=0
    
    # Check each character in the password
    for char in password:
        if char in special_chars:
            special_char_count += 1
        if char.islower():
            lower_count+=1
        if char.isupper():
            upper_count+=1
    return special_char_count+lower_count+upper_count
       

# Test the function
password = "fghjddjjdjdQ?"
count = password_validator(password)
print(f"Number of special characters: {count}")