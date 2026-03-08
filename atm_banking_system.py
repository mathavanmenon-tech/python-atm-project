# ATM Banking System - Beginner Python Project
# Author: Mathavan Selvaraj
# Description: Simple ATM simulation with card validation, password authentication,
# account selection, and basic banking transactions.

print("********** 🏦 Welcome to MIB banking service 🏦**************")

# Asking user to insert ATM card
card = input("Enter your ATM card 💳: ")

# Validate card (case-insensitive)
if card.lower() == "card":
    print("Your card id accepted ✅")

    # Ask for password
    password = int(input("Enter your 4 Digit password 🔑: "))

    # Initial account balance
    balance = 50000

    # Verify password
    if password == 3107:
        print("Password accepted ✅")

        # Dictionary storing account types
        account_type = {1: "Saving account 💰", 2: "Current account 💰"}

        print("Select Account Type")
        for key, value in account_type.items():
            print(key, ":", value)

        # User selects account type
        user_selection = int(input("Enter account type number: "))

        if user_selection in account_type:
            print("You selected:", account_type[user_selection])

            # Transaction menu
            print("\nSelect Transaction")
            print("1. Balance Inquiry 💵")
            print("2. Deposit 💵")
            print("3. Withdrawal 💸")
            print("4. Reset Password")

            option = int(input("Enter option: "))

            # Balance Inquiry
            if option == 1:
                print("Your balance is:", balance)

            # Deposit
            elif option == 2:
                deposit = int(input("Enter your deposit amount: "))
                balance = balance + deposit
                print("Deposit successful ✅")
                print("Updated balance:", balance)

            # Withdrawal
            elif option == 3:
                withdrawal = int(input("Enter your withdrawal amount: "))

                # Prevent withdrawing more than balance
                if withdrawal > balance:
                    print("Insufficient balance ❌")
                else:
                    balance = balance - withdrawal
                    print("Withdrawal successful ✅")
                    print("Remaining balance:", balance)

            # Reset Password
            elif option == 4:
                verification = int(input("Enter your current password: "))

                if verification == 3107:
                    new_password = int(input("Enter new password: "))
                    print("Password reset successful 🔐")
                else:
                    print("Wrong password ❌")

            else:
                print("Invalid transaction option ❌")

        else:
            print("Invalid account type")

    else:
        print("Wrong password ❌")

else:
    print("Invalid card ❌")

print("🙏 Thank you for using MIB Banking Service")