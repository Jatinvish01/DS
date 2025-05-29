# Leap Yaer Checker 

leap_year = int(input("Enter Year: "))

if (leap_year%4 == 0 and leap_year%100 != 0) or leap_year%400 == 0:
      print(leap_year,"is leap year")
else:
      print(leap_year,"is not a leap year")
