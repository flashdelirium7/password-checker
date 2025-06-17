from colorama import Fore, Style, init
init(autoreset=True)

#stylizing the menu
print(Style.BRIGHT + Fore.CYAN + "\n" + "═" * 40)
print("🔐 " + Style.BRIGHT + Fore.WHITE + "Password Creation Guidelines")
print(Fore.CYAN + "═" * 40)

print(Style.BRIGHT + Fore.WHITE + "• At least 8 characters long")
print(Style.BRIGHT + Fore.WHITE +"• Includes both uppercase and lowercase letters")
print(Style.BRIGHT + Fore.WHITE +"• Contain at least one number")
print(Style.BRIGHT + Fore.WHITE +"• Contain at least one special character (!@#$%^&*)")
print(Fore.CYAN + "═" *40)

#creating a function that checks the password to see if it meets requirments
def check_password_requirements(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters long")
    if not any(c.isupper() for c in password):
        errors.append("Include at least one uppercase letter")
    if not any(c.islower() for c in password):
        errors.append("Include at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Include at least one number")
    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password):
        errors.append("Include at least one special character")
    
    if errors:
        return False, errors
    else:
        return True, []

#Prompting the user for their password    
while True:
    userspassword = input(Style.BRIGHT + "Enter your password:")
    if userspassword.lower() == "exit":
        print(Fore.MAGENTA + Style.BRIGHT + "👋 Exiting password setup. Goodbye!")
        break
    
    valid, errors = check_password_requirements(userspassword)

    if valid:
        print(Fore.GREEN + "✅ Password accepted!")
        break
    else:
        print(Fore.RED + Style.BRIGHT + "❌ Password does not meet the requirements:")
        for error in errors:
            print(Style.BRIGHT + f" - {error}")
        print("\nPlease try again.\n")