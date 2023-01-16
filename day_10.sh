#You have a task to make a script to print just local disks device information and how much percentage used from “/opt” directory. The input data is a “df -kh” command output.
#!/bin/bash

# Store the output of the "df -kh" command in a variable
df_output=$(df -kh)

# Use a while loop to read through each line of the output
while read -r line; do
    # Check if the line contains the "/opt" directory
    if echo "$line" | grep -q "/opt"; then
        # Split the line into fields using the delimiter
        fields=($line)
        # Print the device, mount point, and percentage used
        echo "Device: ${fields[0]}"
        echo "Mount point: ${fields[5]}"
        echo "Percentage used: ${fields[4]}"
    fi
done <<< "$df_output"



