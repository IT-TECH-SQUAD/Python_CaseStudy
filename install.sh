#! /usr/bin/bash
null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo -e $b">"$w"  J05-Team-POS - For foodchain services"
echo -e $b">"$w" prepare for installing dependencies ..."
sleep 3
echo -e $b">"$w" Cloning J05-Team-POS "$g"MyCaseStudy"$w
git clone https://github.com/IT-TECH-SQUAD/Case-Study
cd Case-Study
echo -e $b">"$w" installing package: "$g"Requirements"$w
pip install -r requirements.txt
echo -e $b">"$w" successfully installing dependencies"
echo -e $b">"$w" use command "$g"python main.py"$w" to start the console"
