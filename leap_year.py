#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 22, 2022
# This program asks the user for the year and
# determines whether or not that year is a "leap" year or not


def main():
    # Asks user to enter their year
    year_string = input("Enter the year: ")

    # Checks for exceptions
    try:

        # Tries to cast user input into integer
        year = int(year_string)

    # If there are any exceptions
    except Exception:

        # Displays to the user that they did not enter a valid input
        print("Please enter a valid year!")

    # If there are not exceptions
    else:
        # IF the year is evenly divisible by 4
        if year % 4 == 0:

            # IF the year is evenly divisible by 100
            if year % 100 == 0:

                # IF the year is evenly divisible by 400
                if year % 400 == 0:
                    print(f"{year} is a leap year!")
                else:
                    print(f"{year} is not a leap year.")
            else:
                print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
