#TODO: You have a task to make a script to return an array with just local disks device information and how much percentage used from “/opt” directory. The input data is a “df -kh” command output.

import subprocess

# Run the "df -kh" command and store the output in a variable
output = subprocess.check_output(["df", "-kh"]).decode()

# Split the output into lines
lines = output.split("\n")

# Initialize an empty list to store the device information
device_info = []

# Iterate through each line
for line in lines:
    # Check if the line contains the "/opt" directory
    if "/opt" in line:
        # Split the line into fields using whitespace as the delimiter
        fields = line.split()
        # Append the device and percentage used to the device_info list
        device_info.append([fields[0], fields[4]])

# Print the device_info list
print(device_info)
