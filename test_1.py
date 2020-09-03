# # Create an algorithm that takes in integers until the integer is negative.
# When the negetive integer in entered the algorithm stops asking for more integers
# and prints out the highest integer entered and stops.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

while num_int >= 0:
  num_int = int(input("Input a number: "))
  
print("The maximum is", max_int)    # Do not change this line
