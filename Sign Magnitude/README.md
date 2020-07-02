# Sign and Magnitude (Summer 2019, Question 5)
> The concept of positive and negative binary numbers is not formally introduced in CS10. However, the question starts with a detailed explanation of the definition. This justifies the question to be present on a CS10 midterm. Meanwhile, the problem can be directly used in a CS61C exam. 

## Table of Contents
- [Sign and Magnitude (Summer 2019, Question 5)](#Sign-and-Magnitude-Summer-2019-Question-5)
  - [Examples](#examples)
  - [Structure](#structure)
  - [Solutions](#solutions)
  - [How to run on PrairieLearn](#how-to-run-on-prairielearn)

## Examples
	

## Structure
> Names of directories and files (except for png files) a required to remain the same for PL to read

* **info.json**
  * "Title" is the name displayed on the blue [line](#examples)
  * "Topic" is based on course concept map (must have access), you can find it [here](https://docs.google.com/document/d/1B4QBVE2CvoQNXok986j8sVsMYb9662Nd8bFI9nIIj4g/edit).
  * For tag descriptions, go to infoCourse.json in main course directory
  
* **question.html**
  * Question panel element (question text) documentation [here](https://prairielearn.readthedocs.io/en/latest/elements/#pl-question-panel-element)
  * Figure element (images) documentation [here](https://prairielearn.readthedocs.io/en/latest/elements/#pl-figure-element)
  * String input element documentation [here](https://prairielearn.readthedocs.io/en/latest/elements/#pl-string-input-element)
  * Integer input element documentation [here](https://prairielearn.readthedocs.io/en/latest/elements/#pl-integer-input-element)
  
* **server.py**
  * In the first question, a random number in the interval (-100, -50) and (50, 100) is generated. This restricts the variety of difficulty of the question, since the length of the binary number is restricted with no more than 8 digits and no less than 7 digits (including the sign digit). 
  * In the second question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method.
  * In the third question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method. 


## How to run on PrairieLearn

1. Pull course onto local desktop
2. Open local host, follow instructions [here](https://prairielearn.readthedocs.io/en/latest/installing/)
3. Load from disk, click PrairieLearn, and select CS10
4. Under "Questions" button at the top, select "Sign and Magnitude" under QUID 
5. Click "New variant" to see more examples
NOTE: If changes to any .json file is made, Load from disk again

**Contact liaoqitian1024@gmail.com or find Qitian Liao on Slack for questions** 


<!-- 


## Solution Form: 
Fill in the blank. 
## Implementation Description: 
For all the questions, solutions will be automatically computed corresponding to the randomized input. This solution will then be compared with the input of the student for checking and grading purposes. 
 

## Demonstration: 
![alt text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Sign%20Magnitude/Question%20Demo.png "Question Demo") -->