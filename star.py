rows =8  # Number of rows for the pattern

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for printing stars in the current row
        print("*", end="")  # Print star without a new line
    print()  # Move to the next line after each row