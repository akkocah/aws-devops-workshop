#!/bin/bash

# this script creates an account on the local system.
# you will be promted for the account name and password
# Ask for the user name
read -p 'Enter the username to create: ' USER_NAME

#ask for the real name
read -p 'Enter the name of the person who this acoount is for: ' COMMENT

#ask for the password
read -p 'Enter the password to use for the account: ' PASSWORD

#create the user
useradd -c "${COMMENT}" -m ${USER_NAME}

#set the password for the user
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

# Force password change on the first login
passwd -e ${USER_NAME}