sum_ofnumbers = 0
count_i = 0
while True:
    
        num = float(input("Enter a number ( note that -1 will make the program stop): "))
        # Check if the entered number is -1
        if num == -1:
            break
        sum_ofnumbers += num
        count_i += 1

      
# Check if any numbers were entered
if count_i > 0:
    # Calculate the average
    average = sum_ofnumbers/ count_i
    print(f"The average of the numbers entered is: {average}")
else:
    print("No numbers were entered.")