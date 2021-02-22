#!/bin/bash 

#Display the UID and username of the user executing this script
#Display if the user is the root user or not

# Display the UID
echo "Your UID is ${UID}"


# Display the username
USER_NAME=$(id -un)
#USER_NAME=`id -un` #old style
echo "your username is ${USER_NAME} "

# Display the if the user is the root user or not
if [[ "${UID}" -eq 0 ]]
then
    echo 'You are root'
else
    echo 'you are not root.'
fi