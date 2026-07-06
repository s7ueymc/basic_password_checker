import os

# Load the list of common passwords from a text file in the same folder as this script.
def loadCommonPasswords(filename="commonPassword.txt"):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    fullPath = os.path.join(scriptDir, filename)
    with open(fullPath, "r") as file:
        return set(line.strip().lower() for line in file)

# Check how strong a password is and print the results.
def checkPassword(password, commonPasswords):
    # Reject passwords that are too common.
    if password.lower() in commonPasswords:
        print("Password is too common.")
        print("Password strength: Very weak.")
        return

    # Check password characteristics.
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

    # Give the password a score based on the traits it has.
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

    # Translate the score into a simple strength label.
    if score < 2:
        print("Password is weak.")
    elif score < 5:
        print("Password is moderate.")
    else:
        print("Password is strong.")


# Load the common password list once and use it for repeated checks.
commonList = loadCommonPasswords()
checkPassword(input("Enter password: "), commonList)

# Let the user check multiple passwords in one run.
while True:
    choice = input("Do you want to check another password? (y/n): ").strip().lower()
    if choice == 'y':
        checkPassword(input("Enter password: "), commonList)
    elif choice == 'n':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

