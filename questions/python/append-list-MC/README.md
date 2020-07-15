# You can solve this with a pen or append!
> Tests for skills on the **Append** operation of lists (Multiple Choice Version) 

## Table of Contents
- [Variants](#variants)
- [Notes](#Notes)
- [Structure](#structure)
- [How to run on PrairieLearn](#how-to-run-on-prairielearn)
- [Contact](#Contact)
​
## Variants
- The number inside the singleton list ranges in [1, 9]
- The element to be **appended** to the list is either a number or a singleton list with a number 
- The number mentioned above ranges in [1, 9]

<img src="serverFilesQuestion/example1.png">

## Notes
The question checks if the student knows what **append** does, espescially when the element to be **appended** is a list. The **extend** operation will be included in the more difficult version. "**None of these**" and "**error**" will always be among the choices, the other choices are changing dynamically depending on the question

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
