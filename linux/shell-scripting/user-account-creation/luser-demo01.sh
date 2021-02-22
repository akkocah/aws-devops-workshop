#!/bin/bash

# This script displays various information to the screen

# Display 'Hello'
echo 'Hello hasan'
pwd

# Assign a value to a ariable
WORD='script'

#Display that value  using the variable
echo "$WORD"

# Demonstrate that single quotes cause variables to NOT get expanded.
echo '$WORD'

#Combine the variable with hard-coded text.
echo "This is a shell $WORD"

#Display the contens an alternative syntax
echo "This is a shell ${WORD}"

# Append text to the variable
echo "${WORD}ing is a fun!"

# Show hoe NOT to append text to a variable
# this does not working
echo "$WORDing is fun!"

# create the new variable
ENDING='ed'

# combine the two variables
echo "This is ${WORD}${ENDING}"

# change the value stored in the ENDING variable.
ENDING='ing'
echo "${WORD}${ENDING} is fun!"

#Reassign value to ENDING
ENDING='s'
echo "You are going to write many ${WORD}${ENDING} in this class! "