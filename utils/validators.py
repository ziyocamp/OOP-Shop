def validate_name(text: str) -> bool:
    return text.replace(" ", "").isalpha()

def validate_email(email: str) -> bool:
    return "@" in email
