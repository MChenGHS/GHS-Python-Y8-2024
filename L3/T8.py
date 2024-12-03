distance = float(input("What's the total distance of the taxi ride? "))
distance_based_total = 1.8 * distance + 3

time = float(input("How long was the journey in minutes? "))
time_based_total = 0.5 * time + 3

total = min(distance_based_total, time_based_total)
print("Your fare would be ", total, " pounds.")
