# Exam-Generation Project 
This repo includes the auto-generated problems I wrote during Spring 2020. They are supported by PrairieLearn. The following is a more detailed description of each question's implemenations.   

## Sign and Magnitude (Summer 2019, Question 5)
### Question Description:  
The concept of positive and negative binary numbers is not formally introduced in CS10. However, the question starts with a detailed explanation of the definition. This justifies the question to be present on a CS10 midterm. Meanwhile, the problem can be directly used in a CS61C exam. 
### Implementation Description: 
For all the questions, solutions will be automatically computed corresponding to the randomized input. This solution will then be compared with the input of the student for checking and grading purposes. 
1. For the first question, a random number in the interval (-100, -50) and (50, 100) is generated. This restricts the variety of difficulty of the question, since the length of the binary number is restricted with no more than 8 digits and no less than 7 digits (including the sign digit). 
2. For the second question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method.
3. For the third question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method.  

### Demonstration: 
![alt text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Sign%20Magnitude/Question%20Demo.png "Question Demo")

## Number Division (Fall 2019, Question 6)
### Question Description: 
This question focuses on the division of numbers represented in different bases. 
### Implementation Description: 
The numbers I implemented are in binary, octal or hex. The divisor and the dividend are guaranteed to be in different bases. The two numbers are first randomly generated within the range (50, 100). Then they are converted to their base representation depending on their automatically generated bases. 
The solution is generated throughout the process. Student's solutions will be checked up to two significant digits. 
### Demonstration 
![alt text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Number%20Division/Solution%20Demo.png "Question Demo")
