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

2. Solution_2.py contains my solution to problem 2 in the Problem Set which outputs whether or not today is a day beginning with the letter T. The datetime module is used in this solution and there is an if statement used to check whether the current day is Tuesday or Thursday. I used the "or" keyword to check both conditions in the same line. An else statement is used to print an output for the other days of the week that are not given an output as a result of the if statement. 

3. Solution_3.py contains my solution to problem 3 in the Problem Set which prints all numbers between 1,000 and 10,000 that are divisible by 6 but not divisible by 12. In this solution I established a range of numbers between 1,000 and 10,000 and and used an if statement to check the conditions outlined in the program. I used the "and" keyword to check both conditions in one line of code.

4. Solution_4.py asks the user to input any positive integer and outputs the successive values of the following calculation: the current value is taken at each step and if it is even it is divided by 2 and if it is odd it is multiplied by 3 and 1 is added to the value. The program stops when the current value of the number is 1. This is known as Collatz Conjecture and no matter what number is inputted at the beginning of this calculation the result always arrives to 1. I used a while loop and set it to loop as long as the variable which in this case is the integer inputted by the user is greater than 1. Within this loop I used an if statement to identify even numbers with the modulo operator and I used an else statement to pick up all other integers (odd numbers). Within the if and else statements I assigned new values to the variable. When the program executes the loop runs as long as the number inputted by the user is greater than 1 and the results are printed to the screen. I also asked for the original value entered by the user to be printed to the screen first before the execution of the while loop. 

5. Solution_5.py asks the user to input any positive integer and it tells the user if it is a prime number or not. A prime number is a number divisible only by itself and 1. If a number is divisible by any other number it is not a prime number. In this solution a range is established between 2 and one less than the number inputted by the user. A for loop with an if and else statement embedded will run for each number in the range to detect if any number is divisible by the number inputted and the outputs to be printed to the screen have been set accordingly. I have also added a feature whereby if the user enters a negative integer they are prompted to enter only a positive integer. 

6. 

7. Solution_7.py is a program that takes a positive floating point number inputted by the user and outputs an approximation of the square root of that number. In this solution I used the math module to calculate the square root of the number inputted by the user and the round function to round the output to one decimal place. 



## References 
## In this section I detail references and extra reading and research I completed during development of my solutions to this problem set
1. Solution_1.py - This code was adapted from the video we covered in week 4 lectures "loops"
2. Solution_2.py -  I read about the datetime function here: https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python I researched how to use an "or" statement here which allowed me to check for both Tuesday and Thursday in one line: https://www.w3schools.com/python/python_conditions.asp
3. Solution_3.py - In developing my answer to Solution_3.py I read about using "and" to combine logical statements on this website which allowed me to use one line of code to ask for two conditions to be met: https://www.w3schools.com/python/python_conditions.asp
5. Solution_5.py - The code written here is adapted from the lecture we did in week 4 on the break and continue keywords in Python. The code we looked at is shown here: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops I added a line to give the user a a message asking only for a positive number to be inputted if they have entered a negative number. 
7. Solution_7.py - In developing this program I used the math module to calculate the square root of a number inputted by the user. I read about the math.sqrt module here: https://docs.python.org/3/library/math.html I needed the output to be an approximation of the square root and so I used the round function to round the result of the math.sqrt calculation to one decimal place, I read about the round function here: https://www.programiz.com/python-programming/methods/built-in/round