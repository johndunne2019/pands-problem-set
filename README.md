# Problem Set Solutions

This repository contains my solutions to the Problem set 2019 for the module Programming and Scripting at GMIT.
See here for the instructions - https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf.
The problem set consists of ten problems assigned to me as part of my learning in the Programming and Scripting module. I worked to solve all ten problems through a combination of watching the lectures on a weekly basis, extra reading and research online and implementing these learnings in order to develop the solutions to each problem. 

## Readme File
In developing this Readme file I researched how to format the file and what headings should be included at the following links: https://en.support.wordpress.com/markdown-quick-reference/ and https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

## Author
John Dunne

## How to download this repository

1. Go to GitHub
2. Click the download button

## How to run the Code

1. Make sure you have Python installed on your machine

## Contents of my files
**In this section there is a breakdown on the contents of the files in my repository and some background to the contents of each file and the thought process that went into the writing of each file**

**1. Solution_1.py**

 This file contains my solution to problem 1 in the Problem Set which asks the user to input a positive integer and outputs the sum of all numbers between one and that number. In this solution I added a feature to return a message to the user asking them to only enter a positive integer if the number entered by them is less than zero. This feature is an if statement that prints this message to the screen if the user has entered an input less than zero.  In a similar way I have used an if statement to ensure the program is only run where the input is greater than one. I asked for one to be added to the users input and then established a range between 1 and the new value of the variable. The reason I increased the value the user entered by one is because this is necessary to have an accurate range. The sum function is then used to sum all the numbers in the range and print them to the screen. 

**Further reading and references**
* I developed this solution myself and I have included below some links where I did additional reading on if statements, range and sum functions which form a core part of this solution. 
* Sum: https://www.w3schools.com/python/ref_func_sum.asp and https://docs.python.org/3/library/functions.html
* if statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements and https://www.w3schools.com/python/python_conditions.asp
* Range: https://docs.python.org/3/tutorial/controlflow.html#the-range-function and https://www.w3schools.com/python/ref_func_range.asp

**2. Solution_2.py**

 This file contains my solution to problem 2 in the Problem Set which outputs whether or not today is a day beginning with the letter T. The datetime module is used in this solution and within the datetime module I have used the weekday() function to identify the weekday. From my research online I found out the weekday () function returns an integer which corresponds to the day of the week. I used an if statement to check whether the current day is Tuesday or Thursday which in this case is 1 and 3 using the weekday() function. I used the "or" logical operator to check both conditions in the same line. An else statement is used to print an output for the other days of the week that are not given an output as a result of the if statement. 

**Further reading and references**
* I read about the datetime module here: https://docs.python.org/3/library/datetime.html and https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python
* I read about the weekday() function here: https://pythontic.com/datetime/date/weekday
* I researched how to use an "or" statement here which allowed me to check for both Tuesday and Thursday in one line: https://www.w3schools.com/python/python_conditions.asp

**3. Solution_3.py**

This file contains my solution to problem 3 in the Problem Set which prints all numbers between 1,000 and 10,000 that are divisible by 6 but not divisible by 12. In this solution I established a range of numbers between 1,000 and 10,000 and used an if statement to check the conditions outlined in the program. I used the "and" keyword to check both conditions in one line of code. I checked the conditions of the if statement by using the modulo operator to check the remainder when each number in the range was divided by 6 and 12. From my additional reading I learnt that the modulo operator yields the remainder of the division of the first argument by the second argument. Using modulo I was able to ask in the if statement for numbers whose remainder when divided by six was zero and the remainder when divided by twelve was not zero to be printed. 

**Further reading and references**
* I wrote this program myself drawing on learnings from lectures and from extra reading detailed below
* Modulo operator to check remainder after division: https://docs.python.org/3.3/reference/expressions.html
* Range: https://docs.python.org/3/tutorial/controlflow.html#the-range-function and https://www.w3schools.com/python/ref_func_range.asp
* I read about the "and" logical operator here which I used to check both conditions in one line:  https://www.w3schools.com/python/python_conditions.asp

**4. Solution_4.py**

This file contains my solution to problem 4 on the problem set. The program asks the user to input any positive integer and outputs the successive values of the following calculation: the current value is taken at each step and if it is even it is divided by 2 and if it is odd it is multiplied by 3 and 1 is added to the value. The program stops when the current value of the number is 1. This is known as Collatz Conjecture and no matter what number is inputted at the beginning of this calculation the result always arrives to 1. I created a function called odd_even and within the function I set up a while loop and set it to loop as long as the variable which in this case is the integer inputted by the user is greater than 1. Within this loop I used an if statement to identify even numbers with the modulo operator and I used an else statement to pick up all other integers (odd numbers). Within the if and else statements I assigned the new values to the variable in order to complete the calculation. When the function is called the while loop runs as long as the number inputted by the user is greater than 1 and the results are printed to the screen. I also asked for the original value entered by the user to be printed to the screen first before the execution of the while loop. I researched how to have to output printed horizontally in output and learnt that the "end =" command is one way of achieving this. 

**Further reading and references**
* I wrote this program myself drawing on learnings from lectures and from extra reading detailed below
* We covered Functions in week 6 lectures and I did supplementary reading here: https://docs.python.org/3/tutorial/controlflow.html#defining-functions and https://www.youtube.com/watch?v=j2xhtI0WTew&index=12&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_
* While loops: https://docs.python.org/3/reference/compound_stmts.html#while and https://www.w3schools.com/python/python_while_loops.asp
* Modulo operator: https://docs.python.org/3.3/reference/expressions.html
* "end =" to print the output horizontally: https://stackoverflow.com/questions/8437964/python-printing-horizontally-rather-than-current-default-printing

**5. Solution_5.py**

This file contains my solution to problem 5 on the problem set. This program asks the user to input any positive integer and it tells the user if it is a prime number or not. A prime number is a whole number greater than 1 divisible only by itself and 1. If a number is divisible by any other number it is not a prime number. In this solution a range is established between 2 and one less than the number inputted by the user. A for loop with an if statement embedded will run for each number in the range to detect if any number in the range is divisible by the number inputted in which case the number is proven not to be a prime. If no divisor is detected in the if statement the break keyword has been used to break out of the loop and an else statement runs to tell the user the number is a prime. I have also added a feature whereby if the user enters a number less than or equal to 1 they are prompted to enter only a number greater than 1. After watching the week 7 lecture "fstrings" I returned to this solution and changed the format of my output messaged to return the number entered by the user in curly braces. 

**Further reading and references**
* This code is adapted from the example we covered in the week 4 lecture on break and continue keywords - https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
* I have also added a feature whereby if the user enters a number less than or equal to 1 they are prompted to enter only a positive number.
* Break: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops and https://www.w3schools.com/python/python_while_loops.asp



**6. Solution_6.py**

This file contains my solution to problem 6 on the problem set. The program takes a user input string and outputs every second word. I used the .split function that we covered in week 7 lectures in writing this program. The .split function is used to split the string inputted by the user and take only every second word [::2] forming a list of these words. Although we covered the .join function in the week 7 lectures I still struggled to implement this function in the correct way and I had to do some additional research to have this program run correctly. In the end I used the * shortcut to unpack the values in the list that was created by .split and separated them on whitespace with sep ' '. The result of the unpacked list is then printed to the screen as output. As I have separated on whitespace I noticed during testing that punctuation such as quotation marks and commas will be printed to the screen when the program is executed. I could have asked the separator to be a comma but this would not supply the correct output to the user in a case where commas are not used in the input passed in.

**Further reading and references**
* I wrote this program drawing on the material we covered in week 7 lectures and additional reading detailed below:
* We covered the .split and .join functions in week 7 lecture "string operations": https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
* Additional reading on .split: https://www.w3schools.com/python/ref_string_split.asp and https://www.tutorialspoint.com/python/string_split.htm
* Additional reading on .join: https://stackoverflow.com/questions/1876191/what-exactly-does-the-join-method-do and https://www.geeksforgeeks.org/join-function-python/
* I read how to use the shortcut * to unpack lists in python here: https://www.reddit.com/r/learnpython/comments/6b96j3/beginner_how_to_remove_square_bracket_and/, https://thispointer.com/python-how-to-unpack-list-tuple-or-dictionary-to-function-arguments-using/, https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558 and https://stackoverflow.com/questions/3480184/unpack-a-list-in-python. This is the method that I used in the final solution to this problem. 

**7. Solution_7.py**

 This file contains my solution to problem 7 on the problem set. This is a program that takes a positive floating point number inputted by the user and outputs an approximation of the square root of that number. In this solution I used the math.sqrt function within the math module to calculate the square root of the number inputted by the user and the round function to round the output to one decimal place. The program works by asking the user to input a positive floating point number which is assigned a variable. In order to have both the original floating point number entered by the user and the square root both printed to the screen in the output I introduced a second variable which will be used to store the square root value when calculated. In my first attempt at writing the program the output was being printed to the screen in its full form and so I did some additional reading to find out how to have the floating point number output rounded to one decimal place. When the program is executed the 2 variables are printed to the screen - the original value entered by the user and the approximation of the square root of that value. The program runs within a function that I created called sq_root. 
 
**Further reading and references**
* I wrote this program myself using some additional research and reading as outlined below:
* In developing this program I used the math.sqrt function with the math module to calculate the square root of a number inputted by the user.I read about the math module and the math.sqrt function here: https://docs.python.org/3/library/math.html
* I needed the output to be an approximation of the square root and so I used the round function to round the result of the math.sqrt calculation to one decimal place, I read about the round function here: https://www.programiz.com/python-programming/methods/built-in/round
* I added curly brackets when printing the variables after watching the week 7 lecture video "fstrings"

**8. Solution_8.py**

This file contains my solution to problem 8 on the problem set. The program outputs todays date and time in the format - Monday, January 10th 2019 at 1:15pm. We covered the datetime module in the week 6 lecture "modules" and this was the starting point in creating my solution for this problem. In this program I have imported the datetime module and given it the shortened name dt. I used the today() funciton to return the local date and time set and I have asked for today to be printed as output using strftime. strftime is used return a string representation of date and time which we studied in the week 6 lectures "modules". From the week 6 lecture on modules and my extra reading I learnt that the date output can be formatted using the strftime function. I used format tokens to format the output that is printed to the screen to have the week day and month printed in full etc. 

**Further reading and references**
* I wrote this program myself using the example we covered in the week 6 lecture on modules as a starting point and completing additional research and reading online. 
* We covered the datetime module in the week 6 lecture called "modules"
* I completed additional reading on the datetime module here: https://docs.python.org/3/library/datetime.html
* We also covered the strftime function in this week 6 lecture 
* I completed additional reading about strftime here: https://www.w3schools.com/python/python_datetime.asp and https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
* I read about format tokens to format the date output in strftime here: https://stackabuse.com/how-to-format-dates-in-python/ and http://strftime.org/
* I used these format tokens to print the current date and time to the screen in the format requested in the problem

**9. Solution_9.py**

This file contains my solution to problem 9 on the problem set. The program reads in a text file and outputs every second line of the file. The program takes the filename from an argument on the command line. The first thing I did was create a new text file and I used the with open command to open the file in 'w' mode which is write mode. I then asked for a line to be printed to the file. I then reopened the file in 'a' mode which appends text to the existing text in the file. I used backslash n to move to a new line each time I asked for a new line to be printed to the file. In order to have lines printed from the file when the program runs the file should be opened in 'r' mode for reading. I used f.read() to print the full contents of the file to the screen and f.readline() to print one line only. I first wrote my program using a for loop to loop through the file and print all lines as output. I had to complete additional research to see how to have every second line as output. In my finished program a count is set at zero for the first line of the file and a for loop will loop through each line of the file. At each iteration of the for loop one is added to the value of count. An if statement with a modulo operator will check if the line is an even numbered line and if so I have asked for that line to the printed to the screen. The program ends when all lines in the file have been read. An example of how the program works is as follows: The first line of the file has been set as count zero and when the for loop runs for the first time the value of count is set to one first and then an if statement uses the modulo operator to check if the line is assigned an even or odd numbered value. In this case it is an odd number one and so the line is not printed to the screen. On the second iteration of the for loop the value will be an even number and will be printed as output. 

**Further reading and references**
* This program is adapted from extra reading I completed: https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
* I completed this extra reading in order to find out how to have every second line of the file printed as output, I had written the program with a for loop printing all the lines of the file to the screen but I needed extra research to see how to print every second line. 
* We covered this material in the week 7 lecture video- "opening files for reading and writing"
* The with open command is the recommended way to open a file from the command line as the file is closed automatically after operation
* I read about the with open keyword here: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
* I read about writing to a file: https://www.w3schools.com/python/python_file_write.asp
* Reading and writing to files: https://www.youtube.com/watch?v=YV6qm6erphk&index=23&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_ and https://stackabuse.com/read-a-file-line-by-line-in-python/
* I read about reading a file: https://www.w3schools.com/python/python_file_open.asp and https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
