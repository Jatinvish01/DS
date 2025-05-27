# Age Group Categorization
# Classify a person's age group: child (< 13), Teenager (13 - 19), Adult (20-59), senior(60+)

age = int(input("The your age: "))

if (age <= 13 ):
      print(f"Your age is {age}, and You are Children now!")
elif(age <= 20):
      print(f"Your age is: {age}, and You are Teenager!")
elif(age <= 60):
      print(f"Your age is: {age}, and You are Adult!")
else:
      print(f"Your age is: {age}, and your are senior!")