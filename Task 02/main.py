CORRECT_OTP = "4821"


def verify_with_while():
    attempts = 0

    while attempts < 3:
        entered = input("Enter OTP: ")

        if entered.strip() == "":
            print("Blank entry - not counted.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("OTP verified successfully.")
            break

        print("Wrong OTP.")

    else:
        print("Account locked for 30 minutes.")


def verify_with_for():
    for attempt in range(3):
        while True:
            entered = input("Enter OTP: ")

            if entered.strip() == "":
                print("Blank entry - not counted.")
                continue

            break

        if entered == CORRECT_OTP:
            print("OTP verified successfully.")
            break

        print("Wrong OTP.")

    else:
        print("Account locked for 30 minutes.")


def verify_with_security_question():
    attempts = 0
    maximum_attempts = 3

    while attempts < maximum_attempts:
        entered = input("Enter OTP: ")

        if entered.strip() == "":
            print("Blank entry - not counted.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("OTP verified successfully.")
            break

        print("Wrong OTP.")

        if attempts == 3:
            answer = input("Enter your registered city: ")

            if answer.strip().lower() == "chennai":
                maximum_attempts += 2
                print("Two extra attempts granted.")

    else:
        print("Account locked for 30 minutes.")


print("1. While loop")
print("2. For loop")
print("3. Security question")

choice = input("Enter choice: ")

if choice == "1":
    verify_with_while()
elif choice == "2":
    verify_with_for()
elif choice == "3":
    verify_with_security_question()
else:
    print("Invalid choice.")

if False:
    pass
