# Input integer
num_int = int(input("Input a number: "))

max_int = num_int
# When input is above 0, ask for another
# Stop when negative integer is input
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if max_int <= num_int:
        max_int = num_int
    

# Print out inputs
print("The maximum is", max_int)