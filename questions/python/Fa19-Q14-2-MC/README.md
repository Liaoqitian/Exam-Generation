# Take the headache out of lists and strings!
> Tests for skills on String Concatenation (Multiple Choice Version) 

## Table of Contents
- [Variants](#variants)
- [Notes](#notes)
- [Structure](#structure)
- [How to run on PrairieLearn](#how-to-run-on-prairielearn)
- [Contact](#Contact)
​
## Variants
- The length of the list A ranges in [4, 6]
- The numbers in the list range in [0, 1000] and are unique of one another. 
- The index ranges in [1, len(A) - 2]
- The adder ranges in [1, 5]

![alt text](https://github.com/Liaoqitian/Exam-Generation/blob/master/questions/python/Fa19-Q14-2-MC/serverFilesQuestion/demo.png "Question Demo")

## Notes 
The question tests the student's ability to distinguish string concatenation from normal arithmetic addition. Whether the student includes quotation marks in the solution is not something the question intends to test on. Thereofore, there will only be one correct solution with quotation marks. Its counterpart without quotation marks is intentionally left out.

## Structure
> Names of directories and files (except for png files) a required to remain the same for PL to read
​
- [**info.json**](info.json)
  - "Title" is the name displayed on the blue [line](#part-1)
  - "Topic" is based on course [concept map](https://docs.google.com/document/d/1B4QBVE2CvoQNXok986j8sVsMYb9662Nd8bFI9nIIj4g/edit) (access required)
  - For tag descriptions, see infoCourse.json in main course directory
​
- [**question.html**](question.html)
  - Question panel element (question text) documentation [documentation](https://prairielearn.readthedocs.io/en/latest/elements/#pl-question-panel-element)
  - Multiple Choice Element documentation [documentation](https://prairielearn.readthedocs.io/en/latest/elements/#pl-multiple-choice-element)
​
- [**server.py**](server.py)
  - Question generator file, with all of the randomization components.
  - Make changes here if adding or deleting variants to clientFilesQuestion
​
- [**serverFilesQuestion**](serverFilesQuestion)
  - Examples for README.md and solutions (explains the logic for solving)
  - Not available to students

## How to run on PrairieLearn
1. Pull course onto local desktop
2. Open local host, follow instructions on [PrairieLearn](https://prairielearn.readthedocs.io/en/latest/installing/) or on the main directory's README.md file.
3. Load from disk, click PrairieLearn, and select CS10
4. Under "Questions" button at the top, select "predicate_mystery_replace" under QUID
5. Click "New variant" to see the other variants 
NOTE: If changes to any .json file is made, Load from disk again
​

## Contact
Contact via liaoqitian1024@gmail.com or find Qitian Liao on Slack channel. 
