# Fruits Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unrip based on its color. (e.g., Banana: Green-Unripe, Yeellow - Ripe, Brown-Overripe)

fruit = "Banana"
color = "Green"

if fruit == "Banana":
      if color == "Green":
            print("The Banana is Unripe")
      elif color == "Yellow":
            print("The Banana is Ripe")
      elif color == "Brown":
            print("The Banana is Overripe")
else:
      print("Invalid Fruit name")