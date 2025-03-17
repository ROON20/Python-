import re

def assess_password_strength(password):
    """Assess the strength of the given password and provide feedback."""
    
    # Define criteria
    min_length = 8
    max_length = 20
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check for repeated characters
    has_repeated_chars = len(set(password)) < len(password)
    
    # Check for sequences (e.g., "abc", "123")
    has_sequence = bool(re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password, re.IGNORECASE))
    
    length = len(password)
    length_criteria = min_length <= length <= max_length

    # Assess strength
    if length_criteria and has_uppercase and has_lowercase and has_digit and has_special_char and not has_repeated_chars and not has_sequence:
        return "Strong: Your password meets all the criteria."
    elif length_criteria and (has_uppercase or has_lowercase) and (has_digit or has_special_char) and not has_repeated_chars and not has_sequence:
        return "Moderate: Your password is fairly strong but could be improved by adding more complexity."
    elif length_criteria or (has_uppercase or has_lowercase) or (has_digit or has_special_char):
        if has_repeated_chars or has_sequence:
            return "Weak: Your password contains repeated characters or common sequences. Consider making it longer and adding more diverse characters."
        return "Weak: Your password does not meet enough criteria. Consider making it longer and adding more diverse characters."
    else:
        return "Very Weak: Your password is too short and lacks complexity. Make sure it's at least 8 characters long and includes a mix of uppercase letters, lowercase letters, digits, and special characters."

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter the password to assess: ")
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == '__main__':
    main()
