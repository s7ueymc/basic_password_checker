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

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if hasUpper:
        score += 1
    if hasLower:
        score += 1
    if hasDigit:
        score += 1
    if hasSpecial:
        score += 1
    
    print("Password strength score:", score, "/6")

    if score < 2:
        print("Password is weak.")
    elif score < 5:
        print("Password is moderate.")
    else:
        print("Password is strong.")

checkPassword(input("Enter password: "))
