import prairielearn as pl
import random, copy, math

def enquote_string(s):
    if type(s) == str:
        return '"' + s + '"'
    else:
        return s
# only use after ensuring that s is a string
def parse_quoted(s):
    s = s.strip()
    if len(s) == 0 or len(s) == 1:
        return (False,"Malformed input: put string in quotes","")
    if s[0] != s[len(s)-1] or s[0] not in ['"', "'"]:
        return (False,"Malformed input: put string in matching quotes","")
    quote_char = s[0]
    opposite_char = '"' if quote_char == "'" else "'"
    escaped_quote_token = "\\" + quote_char
    s_copy = s[1:-1]
    s_copy = s_copy.replace(escaped_quote_token, "")
    if s_copy.find(quote_char) != -1:
        return (False,"Malformed input: If you use the same quotation mark character internally, escape it with a single backslash: \\","")
    return (True,s,s[1:-1])

def generate(data):

    # Sample a list of random length between 3 and 5. 
    length = random.randint(3, 6)

    # Sample random elements in (0, 1000) to fill the list. 
    A = [0] * length
    copy = [0] * length
    copy = random.sample(range(0, 1000), length)
    for i in range(length): 
        A[i] = str(copy[i])

    # Set up the question. 
    index = random.randint(1, len(A) - 2)
    adder = str(random.randint(1, 5))
    
    # Compute the correct solution.
    
    solution = A[index] + adder
    data['params']['raw_solution'] = solution
    solution = str([solution]).replace("[","").replace("]","")
    
    # Store the parameters.
    A = str(A).replace("'", '"')
    data['params']['A'] = A
    data['params']['index'] = index
    data['params']['adder'] = adder 
    data['correct_answers']['solution'] = solution.replace("'",'"')

def grade(data):
    if data['score'] == 0: 
        if data["submitted_answers"]["solution"] == data['correct_answers']['solution'].replace('"',"'"):
            data["partial_scores"]["solution"]["score"] = 1
            data["score"] = 1
            data["feedback"]["solution"] = "you got this correct!"
        elif data["submitted_answers"]["solution"] == data['params']['raw_solution']:
            data["partial_scores"]["solution"]["score"] = 1
            data["score"] = 1
            data["feedback"]["solution"] = "Remember the quotation marks next time!"
        else:
            data["feedback"]["solution"] = "you got this wrong, sorry"