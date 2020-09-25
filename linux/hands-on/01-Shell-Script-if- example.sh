#!/bin/bash
read -p "Enter your name: " name
read -p "Enter your age: " age
read -p "Enter Avarege Life Expectancy: " ale
if (( age < 18 ))
then
        echo "$name you must be a student"
        echo "at least $(( 18 - age )) years to become a worker"
elif (( (( age >= 18 )) && (( age < 65 )) ))
then
        echo "$name you must be a worker."
        echo "$(( 65 - age )) years to retire."
elif (( age >= 65 ))
then
        if (( age < ale ))
        then
                echo "Retired"
                echo "$(( ale - age )) year to DIE"
        else
                echo -ne '\007'
                echo "!!!!! Already DIED !!!!!"
                sleep 3
                echo -ne '\007'
                echo "!!!!! Already DIED !!!!!"
                sleep 3
                echo "!!!!! Already DIED !!!!!"
                echo -ne '\007'
        fi
fi