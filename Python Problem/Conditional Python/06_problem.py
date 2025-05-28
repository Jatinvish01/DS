# Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance (e.g., <3ikm; walk, 3-15km: km:car).

distance = int(input("Enter the Distance: "))

if distance < 3:
      transport = "Walk"
elif distance < 15:
      transport = "Bike"
elif distance >= 15:
      transport = "Car"

print(transport)
