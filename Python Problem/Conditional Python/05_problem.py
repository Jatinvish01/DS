# Weather Aacitvity Suggestion
# Suggest an activity based on the weather (e,g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

weather = (input("Enter the season (Sunny, Rainy and Snowy): "))

if weather == "Sunny":
      activity = " Go for Walk"
elif weather == "Rainy":
      activity = "Read a books"
elif weather == "Snowy":
      activity = "Build snowman"

print(activity)