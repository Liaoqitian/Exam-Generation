# Prairielearn Questions for CS10

## Structure

> Names of directories and files (except for png files) are required to remain the same for PL to read

- [**info.json**](https://prairielearn.readthedocs.io/en/latest/question/#question-infojson)
  - Generate a [UUID](https://www.uuidtools.com/generate/v4)
  - The title should be a joke relevant to the question, students can see this
  - Topics can be found in both in the [concept map](https://docs.google.com/document/d/1B4QBVE2CvoQNXok986j8sVsMYb9662Nd8bFI9nIIj4g/edit) and [infoCourse.json](../infoCourse.json)
  - [Tags](#tagging-conventions) are defined in [infoCourse.json](../infoCourse.json) and should follow the order listed
  - All topics are capitalized and all tags are lowercase
  - Type will always be v3 unless otherwise noted

- [**question.html**](https://prairielearn.readthedocs.io/en/latest/question/#question-questionhtml)
  - Template for question on PrairieLearn
  - Use PrairieLearn's [elements for writing questions](https://prairielearn.readthedocs.io/en/latest/elements/)

- [**server.py**](https://prairielearn.readthedocs.io/en/latest/question/#question-serverpy)
  - Question generator file, with all of the randomization components.
  - Make changes here if changing randomized components

- [**clientFilesQuestion**](clientFilesQuestion)
  - Files/pictures needed to create QG
  - Files here are vailable to students
  - Make changes to server.py if adding images to this directory

- [**serverFilesQuestion**](serverFilesQuestion)
  - Examples for README.md
  - Solution files (explains the logic for solving)
  - Files here not available to students

## Topic Conventions

The top-level `infoCourse.json` of this repo defines topics that serve as umbrella terms for colored nodes in the [concept map](https://docs.google.com/document/d/1B4QBVE2CvoQNXok986j8sVsMYb9662Nd8bFI9nIIj4g/edit)

- ALL topics should be capitalized for consistency throughout the course repo.

- To find the topic that corresponds to the particular node for your question, use command+f(mac) or control+f(windows) on `infoCourse.json` and type the name of that node.
  - Ex: Search 'Roboto Tracing' and you will find that the corresponding topic is 'Logical Procedures'

## Tagging Conventions

The top-level `infoCourse.json` of this repo defines a few "global" tags that all questions should have.  This will help curation of questions in the future, so please *follow these guidelines* when adding tags to each question's `info.json`.

- ALL tags should be lowercase for consistency throughout the course repo.

- To find a specific topic/tag and follow format rules, use command+f(mac) or control+f(windows) on `infoCourse.json` and type in a key word.
  - EX: to find 'OOP object' tag, type in 'oop'

NOTE: Symbols are NOT allowed on tags, they will make the search bar on PL questions dissappear

### Required Tags

1. Type of assessment:
   - formative (Non-graded level, public)
   - summative (Exam level, secret)
2. Type of exam question:
   - quest
   - midterm
   - final
3. Difficulty of the question relative to class pace:
   - easy
   - medium
   - hard
4. Answer format tag: (tag multiple for multiple elements)
   - radio --> single select multiple choice
   - checkbox --> multiple select multiple choice
   - blank --> input box (string, integer, symbol, ect.)
   - dead python
   - dropdown
   - matrix
   - drawing (The answer format requires drawing on a canvas to input a graphical representation of an answer.)
5. Stage of completion:
   - alpha (question is ready for TA review)
   - beta (question is ready for instructor to review)
   - release (instructor has blessed the question and can now be released to students)
6. Any subtopics not covered in the Topics section of `infoCourse.json` should be defined on `infoCourse.json`. Only tag the most relevant subtopic on `info.json`.
7. Author name as Github username (ex: 'ddgarcia' for Dan Garcia's Github). All developers should define their author tag inside `infoCourse.json`
8. Institution's name: 'Berkeley'
9. Semester the question was written in and the question number (Ex: Fa18Q6 or Sp20Q10 or Su20)
   - Usually the 'type of exam' tag goes hand in hand with this one.
   - These should not be defined in `infoCourse.json` and only tagged in `info.json`.
10. Conceptual v Numerical variants (ex: 4v5)
   - Conceptual variants are the number of times the prompt changes in a QG
   - Numerical variants are the number of times the values in a QG change.
   - If every conceptual variant has 5 numerical variants and we have 4 conceptual variants, we get "4v5"
   - These should not be defined in `infoCourse.json` and only tagged in `info.json`.

NOTE: Any tags not defined in `infoCourse.json` but tagged in `info.json` will default to the gray1 color.