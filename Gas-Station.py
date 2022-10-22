# ////////////////////////////////////////
# //                                    //
# // Name: Sabaudo Matteo               //
# //                                    //
# // Assignment: Gas Station System     //
# //                                    //
# ////////////////////////////////////////

import os
import sys

fuel = 1500
balance = 50000
status = "Active"
price = 3.826

option = True

while option:
    os.system('cls')

    print("\nGAS STATION SYSTEM")

    print("\n---------------------------------------------")
    print("\n 1. Money Balance\n 2. Fuel Status\n 3. System Stats\n 4. Admin Options\n 5. Exit")
    print("\n---------------------------------------------")
    option = input("\nSelect An Option: ")

    if option == "1":
        os.system('cls')
        print(f"\nThe actual balance is: ${balance:.2f}")
        print()
        os.system("pause")

    elif option == "2":
        os.system('cls')
        print(f"\nThe actual fuel status is: {fuel:.2f} L")
        print()
        os.system("pause")

    elif option == "3":
        os.system('cls')
        print(f"\nActual status is: {status}")
        print()
        os.system("pause")

    elif option == "4":
        os.system('cls')
        username = input("\nUsername: ").lower()
        pwd = input("Password: ")

        if username == "admin:matteosabaudo" and pwd == "root":
            op = True

            while op:
                os.system('cls')

                print("\nGAS STATION SYSTEM")

                print("\n--------------------------------------------------------------------------------")
                print("\n1. Balance\n2. Deposit \n3. Withdraw\n4. Change System Status\n5. Fuel Controls ")
                print("\n--------------------------------------------------------------------------------")
                op = input("\nSelect An Option: ")

                if op == "1":
                    os.system('cls')
                    print(f"\nActual Balance: ${balance:.2f}")
                    os.system("pause")

                elif op == "2":
                    os.system('cls')
                    deposit = float(input("How much would you like to deposit? "))
                    if deposit > 0:
                        balance += deposit
                        print(f"\nTotal Added: ${deposit:.2f}")
                        print(f"Actual Balance: ${balance:.2f}")
                        os.system("pause")
                    else:
                        print(f"\nTotal Added: ${deposit:.2f}")
                        print(f"Actual Balance: ${balance:.2f}")
                        os.system("pause")

                elif op == "3":
                    os.system('cls')
                    withdraw = float(input("How much would you like to withdraw? "))
                    if deposit > 0:
                        balance -= withdraw
                        print(f"Total Withdraw: ${withdraw:.2f}")
                        print()
                        os.system("pause")
                    else:
                        print(f"Total Withdraw: ${withdraw:.2f}")
                        print()
                        os.system("pause")

                elif op == "4":
                    if status == "Active":
                        change_status = input("\nWould you like to change the system stats to Inattive? (Y/N) ").lower().strip()
                    if change_status == "yes" or change_status == "y":
                        status = "Inattive"
                        print(f"\n[ADMIN] The status is changed to: {status}!")
                        print()
                        os.system("pause")
                    else:
                        os.system('cls')

                elif op == "5":
                    os.system('cls')
                    print(f"\nPrice for liter: {price:.2f}")

                    print(f"\nActual quantity of fuel in the central tank: {fuel:.2f} L")
                    fuel_control = float(input("\nTotal amount in liters to fuel the central tank: "))
                    total = fuel_control * price
                    balance -= total
                    fuel += total
                    if fuel_control > 0:
                        print("\nCONTROL PANEL RESULTS: ")
                        print(f"\nTotal Fuel Added: {fuel_control:.2f} L")
                        print(f"Total Paid: ${total:.2f}")
                        print(f"Central fuel tank: {fuel:.2f}")
                        print(f"Actual Balance: ${balance:.2f}")
                        print()
                        os.system("pause")
                    else:
                        print("\nCONTROL PANEL RESULTS: ")
                        print(f"\nTotal Fuel Added: {fuel_control:.2f} L")
                        print(f"\nTotal Paid: ${total:.2f}")
                        print(f"Central fuel tank: {fuel:.2f}")
                        print(f"Actual Balance: ${balance:.2f}")
                        print()
                        os.system("pause")
        else:
            print("\n[ERROR] Username and/or Password Incorrect!")
            print()
            sys.exit()

    elif option == "5":
        print()
        sys.exit()