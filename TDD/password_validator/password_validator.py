special_chars = [
    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', '|', '\\',
    ':', ';', '"', "'",
    '<', '>', ',', '.', '?', '/'
]


def is_password_secure(password):
    # Initialize counter for special characters
    special_char_count = 0
    lower_count=0
    upper_count=0
    digit_count=0
    password_is_greater=True
    
    # Check each character in the password
    if len(password)>=8:
        password_is_greater=True
    else:
        password_is_greater=False
        
    for char in password:
        if char in special_chars:
            special_char_count += 1
        elif char.islower():
            lower_count+=1
        elif char.isupper():
            upper_count+=1
        elif char.isdigit():
            digit_count+=1

    has_special=special_char_count>=1
    has_digit=digit_count>=1
    has_lower=lower_count>=1
    has_upper=upper_count>=1
    
    is_secure=(password_is_greater and has_special and has_digit and has_lower and has_upper)
    return is_secure

   
       

# Test the function
password = "fgT!3dd1"
count = is_password_secure(password)
print(f"The password is secure? {count}" )