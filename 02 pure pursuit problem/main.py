import random
import math

# Initialize flag to control the loop (0 = keep running, 1 = terminate)
flag = 0

# Initialize the time counter
time = 0

# Speed of the fighter plane (constant velocity)
vf = 20

# Generate random initial positions for both planes
# Fighter plane's initial position (xf, yf)
xf = random.randint(1, 1000)
yf = random.randint(1, 1000)

# Bomber plane's initial position (xb, yb)
xb = random.randint(1, 1000)
yb = random.randint(1, 1000)

# Main loop for simulating the pursuit
while flag == 0:
    # Calculate the Euclidean distance between the fighter and the bomber planes
    distance = math.sqrt((xf - xb) ** 2 + (yf - yb) ** 2)

    # Check if the fighter is close enough to shoot down the bomber
    if distance <= 100:
        print("The fighter plane shot down the bomber at time", time)
        flag = 1  # Set flag to 1 to stop the loop

    # Check if the bomber has escaped (distance greater than 1000 units)
    elif distance > 1000:
        print("The bomber plane escaped at time", time)
        flag = 1  # Set flag to 1 to stop the loop

    else:
        # Update fighter plane's position
        # The fighter moves towards the bomber by calculating the direction
        # The new position is updated based on the ratio of the current distance
        xf = xf + vf * (xb - xf) / distance  # Move in x direction towards bomber
        yf = yf + vf * (yb - yf) / distance  # Move in y direction towards bomber

        # Randomly update the bomber's position
        # The bomber moves randomly, potentially changing its course
        xb = random.randint(1, 1000)
        yb = random.randint(1, 1000)

        # Increment the time counter by 1 unit for each iteration
        time += 1
