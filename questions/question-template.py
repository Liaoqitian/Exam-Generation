import sys
import os

"""
This function creates all files and subfolders for a new QG.
Enter your questions QUID such as 'snap/iteration/new_question'. 
Make sure all parent directories exist beforehand 
('snap' & 'iteration' would already exist)
"""
def question_template(quid):
    os.chdir('questions/python')
    split_dir = quid.split("/")
    for folder in split_dir:
        if os.path.isdir(folder):
            os.chdir(folder)
        else:
            os.mkdir(folder)
            os.chdir(folder)

    server = open('server.py', 'w')
    question = open('question.html', 'w')
    info = open('info.json', 'w')
    readme = open('README.md', 'w')
    os.mkdir('clientFilesquestion')
    os.mkdir('serverFilesquestion')

    server.write("""import random 
def generate(data):
    return data
    """)
    question.write("""<html>
    <head>
        <style>
            pre {
                font-size: 110%;
            }
            code {
                color: black;
                padding: 2px;
                font-size: 110%;
            }
        </style>
        <link rel="stylesheet" href="./styles.css">
    </head>
<body>
<pl-question-panel>
</pl-question-panel>
""")
    info.write("""{
    "uuid": "REPLACE",
    "title": "",
    "topic": "",
    "tags": ["liaoqitian", "final", "blank", "easy", "formative", "berkeley", "alpha", "Fa14Q12"],
    "type": "v3"
}
""")
    readme.write("""# Title
> Description
## Table of Contents
## Examples
## Solutions
## Contact liaoqitian1024@gmail.com or find Qitian Liao on Slack for questions
""")

question_template('dictionary-key-value-pair')