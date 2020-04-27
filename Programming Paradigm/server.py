import random, copy, math
import numpy as np

def generate(data):
    # The following are the four possible questions represented in strings
    q_1 = "Easily program 1,000 computers because reporter and predicate outputs are only due to inputs, not to any previous states."
    q_2 = "Putting data in which can be queried later, like finding all your cousins from your family tree. "
    q_3 = "Drawing a complicated picture on the screen using pen up/down and move/turn commands. " 
    q_4 = "Authoring a role-playing game with different interacting creatures, like zombies & skeletons. "
    Questions = [q_1, q_2, q_3, q_4]

    # The following are the four corresponding solutions represented in strings s
    a_1 = "Functional"
    a_2 = "Declarative"
    a_3 = "Imperative"
    a_4 = "Object-Oriented"
    Solutions = [a_1, a_2, a_3, a_4]

    # Randomize the sequence of questions 
    idx = np.random.permutation(4)

    # Put the questions into data['params'] in the randomized order
    Question1 = Questions[idx[0]]
    Question2 = Questions[idx[1]]
    Question3 = Questions[idx[2]]
    Question4 = Questions[idx[3]]
    data['params']['Question1'] = Question1 
    data['params']['Question2'] = Question2
    data['params']['Question3'] = Question3
    data['params']['Question4'] = Question4

    # Put the solutions into data['correct_answers'] in the corresponding order
    Answer1 = Solutions[idx[0]]
    Answer2 = Solutions[idx[1]]
    Answer3 = Solutions[idx[2]]
    Answer4 = Solutions[idx[3]]

    data['params']['Answer1'] = Answer1 
    data['params']['Answer2'] = Answer2
    data['params']['Answer3'] = Answer3 
    data['params']['Answer4'] = Answer4