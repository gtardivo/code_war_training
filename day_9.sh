# This script uses the -e option for the [ command to check if the file "auth.log" exists in the current directory which is "/var/log/".

# If the file exists, the script will output "auth.log exists."
# If the file does not exist, the script will output "auth.log is vanished."
# You can run this script by saving it to a file with the extension .sh, give it the execution permissions and run it.

#!/bin/bash

if [ -e "auth.log" ]
then
  echo "auth.log exists."
else
  echo "auth.log is vanished."
fi
