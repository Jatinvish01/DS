# Pet Food Recommandation

dog = int(input("Enter the age of dog: "))
cat = int(input("Enter the age of cat: "))

if dog < 2:
      print("They eat only puppy food")
elif dog >= 2:
      print("Eat senior dog food")

elif cat > 5:
      print("Eat Senior cat food only")
elif cat <= 5:
      print("Eat junior food only")
else:
      print("Invalid")
      