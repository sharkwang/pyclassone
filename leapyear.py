#!/usr/bin/python3

year = int(input("Which year?"))


if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
	print(f"The {year} is leap year.")
else:
	print(f"The {year} is NOT leap year.")
