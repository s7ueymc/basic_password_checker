def checkPassword(password):
    length = len(password)
    hasUpper = any(c.isupper() for c in password)
    hasLower = any(c.islower() for c in password)
    hasDigit = any(c.isdigit() for c in password)
    hasSpecial = any(not c.isalnum() for c in password)

    print("Password length:", length)
    print("Has uppercase:", hasUpper)
    print("Has lowercase:", hasLower)
    print("Has digit:", hasDigit)
    print("Has special character:", hasSpecial)

checkPassword(input("Enter password: "))
