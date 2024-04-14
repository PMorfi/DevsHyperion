"""Pseudocode:

1. Prompt the user to enter the time (in minutes) for swimming event and store it in a variable swim_time.
2. Prompt the user to enter the time (in minutes) for cycling event and store it in a variable cycle_time.
3. Prompt the user to enter the time (in minutes) for running event and store it in a variable run_time.
4. Calculate the total time by adding swim_time, cycle_time, and run_time, and store it in a variable total_time.
5. Check the total_time against the qualifying criteria and determine the award:
   a. If total_time is within 0-100 minutes, set award as "Provincial colours".
   b. If total_time is within 101-105 minutes, set award as "Provincial half colours".
   c. If total_time is within 106-110 minutes, set award as "Provincial scroll".
   d. If total_time is more than 110 minutes, set award as "No award".
6. Display the determined award."""

# Read in the times for swimming, cycling, and running
swimming_time = int(input("Enter swimming time (minutes): "))
cycling_time = int(input("Enter cycling time (minutes): "))
running_time = int(input("Enter running time (minutes): "))

# Calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# Determine the award based on the total time taken
if total_time <= 100:
    award = "Provincial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

# Display the award
print("Total time taken:", total_time, "minutes")
print("Award:", award)
