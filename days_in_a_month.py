#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: April 2022
# This program tells you how many days there are in a month
#   with user input


def main():
    # This creates the program

    # input
    name_of_month = input("Tell me a month on the calendar (ex: January): ")

    # process
    if name_of_month == "January":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "February":
        print(
            "\nThe number of days in this month is 28, unless it is a leap year. Then it is 29 days."
        )

    elif name_of_month == "March":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "April":
        print("\nThe number of days in this month is 30.")

    elif name_of_month == "May":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "June":
        print("\nThe number of days in this month is 30.")

    elif name_of_month == "July":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "August":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "September":
        print("\nThe number of days in this month is 30.")

    elif name_of_month == "October":
        print("\nThe number of days in this month is 31.")

    elif name_of_month == "November":
        print("\nThe number of days in this month is 30.")

    elif name_of_month == "December":
        print("\nThe number of days in this month is 31.")


if __name__ == "__main__":
    main()
