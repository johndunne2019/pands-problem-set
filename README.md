# Problem Set Solutions

This repository contains my solutions to the Problem set 2019 for the module Programming and Scripting at GMIT.
See here for the instructions - https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

## How to download this repository

1. Go to GitHub
2. Click the download button

## How to run the Code

1. Make sure you have Python installed on your machine

## Contents of my files

1. Solution_1.py contains my solution to problem 1 in the Problem Set which asks the user to input a positive integer and outputs the sum of all numbers between one and that number. 

2. Solution_2.py contains my solution to problem 2 in the Problem Set which outputs whether or not today is a day beginning with the letter T. 

3. Solution_3.py contains my solution to problem 3 in the Problem Set which prints all numbers between 1,000 and 10,000 that are divisible by 6 but not divisible by 12. 

4. Solution_4.py asks the user to input any positive integer and outputs the successive values of the following calculation: the current value is taken at each step and if it is even it is divided by 2 and if it is odd it is multiplied by 3 and 1 is added to the value. The program stops when the current value of the number is 1. This is known as Collatz Conjecture and no matter what number is inputted at the beginning of this calculation the result always arrives to 1.

5. Solution_5.py asks the user to input any positive integer and it tells the user if it is a prime number or not. A prime number is a number divisible only by itself and 1. If a number is divisible by any other number it is not a prime number.



## References 
1. Solution_1.py - This code was adapted from the video we covered in week 4 lectures "loops"
2. Solution_2.py -  I read about the datetime function here: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python I researched how to use an "or" statement here which allowed me to check for both Tuesday and Thursday in one line: https://www.w3schools.com/python/python_conditions.asp
3. Solution_3.py - In developing my answer to Solution_3.py I read about using "and" to combine logical statements on this website which allowed me to use one line of code to ask for two conditions to be met: https://www.w3schools.com/python/python_conditions.asp
5. Solution_5.py _ The code written here is adapted from the lecture we did in week 4 on the break and continue keywords in Python. The code we looked at is shown here: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops