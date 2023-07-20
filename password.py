def main():
    try:
        desired_length = int(input("Enter the desired password length: "))
        if desired_length <= 0:
            print("Password length should be a positive number.")
            return

        password = input("Enter the password (should be {} characters long): ".format(desired_length))
        if len(password) != desired_length:
            print("Password length doesn't match the desired length.")
        else:
            print("Password set successfully:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()