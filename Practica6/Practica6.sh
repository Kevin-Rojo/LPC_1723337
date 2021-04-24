#!/bin/bash

ip address
hostname -I
curl ifconfig.me


nmap -F -oN nmap_result.txt 10.0.0.1

openssl enc -base64 -in nmap_result.txt -out nmap_result
