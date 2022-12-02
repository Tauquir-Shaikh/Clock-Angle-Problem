def calculate_angle(h, m):
#If the entered value is in negative it's Invalid
    if (h < 0 or m < 0):
        return ('Invalid input')

    if (h > 12):                # Changing the value in 12 hour format
        h -= 12
    if (m > 60):
        m -= 60

    hour_angle = 0.5 * (h * 60 + m)       # Calculating the Hour angle
    minute_angle = 6 * m                  # Calculating the minute angle

    angle = abs(hour_angle - minute_angle)   # Storing the Angle betweeen them without sign

    angle = min(360 - angle, angle)      # Changing the Angle betweeen them in the range 0-180 degrees

    return angle

#Taking the input for time from the user
time = input("Enter time in hh:mm format: ")

#Storing the Hour and Minute values in different variables
h, m = map(int,time.split(":"))

#Printing the Angular Difference
print(f"The Shorter angle between the Hour hand and Minute hand is {calculate_angle(h, m)} degrees")
