#!/bin/bash

read -p "Enter your pem file located directory : " pem_path
cd $pem_path

read -p "Enter EC2 ip: " ec2_ip
read -p "Enter your pem file name : " pem_name

ssh -i $pem_name ec2-user@$ec2_ip
