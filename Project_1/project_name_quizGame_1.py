 # QUIZ GAME PROJECT
def run_quiz(questions): 
    score  = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct Answer \n")
            score += 1
        else:
            print("Wrong! The correct answer is ", question["answer"],"\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        "prompt": "What is the correct syntax to print 'Hello, World!' in Python?",
        "options": ["A. print(Hello, World!)","B) ec ho('Hello, World!')","C) display('Hello, World!')","D) write('Hello, World!')"],
        "answer": "A"
    },
    {
        "prompt": "Which of the following is a valid variable name in Python?",
        "options": ["A. 2variable","B. _variable","C. variable-name","D. variable name"],
        "answer": "B"
    },
    {
        "prompt": "What will the following code output: 5 + 3 * 2?",
        "options": ["A. 16","B) 11","C) 13","D) 10"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following data types is mutable in Python?",
        "options": ["A) Integer","B) Float","C) String","D) List"],
        "answer": "D"
    },
    {
        "prompt": "What will be the output of the following code: len('Python')?",
        "options": ["A) 7","B) 6 ","C) 5 ","D) 4 "],
        "answer": "C"
    },
     {
        "prompt": "What does the range() function in Python return?",
        "options": ["A) A list of integers","B)  A tuple of integers","C) A dictionary of integers","D) An iterator of integers"],
        "answer": "D"
    },
    {
        "prompt": "What is the output of the following code: 'hello' + 'world'?",
        "options": ["A) hello world","B) helloworld","C) hello + world","D) SyntaxError"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following is NOT a valid Python data type?",
        "options": ["A) Tuple","B) Array","C) Set","D) Dictionary"],
        "answer": "B"
    },
    {
        "prompt": "What is the result of the expression: 10 / 3?",
        "options": ["A) 3.333","B) 3","C) 3.0","D) 3.33"],
        "answer": "A"
    },
    {
        "prompt": "What is the keyword used to define a function in Python?",
        "options": ["A) func","B) define","C) function","D) def"],
        "answer": "D"
    },
    {
        "prompt": "Which built-in function is used to sort a list in Python?",
        "options": ["A) sort()","B) sorted()","C) arrange()","D) order()"],
        "answer": "B"
    },
    {
        "prompt": "What will be the output of the following code: 'Python'.lower()?",
        "options": ["A) python","B) PYTHON","C) Python","D) SyntaxError"],
        "answer": "A"
    },
    {
        "prompt": "Which symbol is used for single-line comments in Python?",
        "options": ["A) //","B) /* */","C) #","D) <!-- -->"],
        "answer": "C"
    },
    {
        "prompt": "What is the output of the following code: bool('False')?",
        "options": ["A) True","B) False","C) SyntaxError","D) TypeError"],
        "answer": "A"
    },
    {
        "prompt": "Which method is used to remove an element from a list in Python?",
        "options": ["A) pop()","B) remove()","C) delete()","D) erase()"],
        "answer": "A"
    },
    {
        "prompt": "What is the correct way to open a file named 'data.txt' for writing in Python?",
        "options": ["A) open('data.txt', 'r')","B) open('data.txt', 'w')","C) open('data.txt', 'a')","D) open('data.txt', 'x')"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following is NOT a valid Python keyword?",
        "options": ["A) if","B) else","C) elif","D) then"],
        "answer": "D"
    },
    {
        "prompt": "What will be the output of the following code: 'Python'[2:]?",
        "options": ["A) 'Py'","B) 'tho'","C) 'thon'","D) 'Pyth'"],
        "answer": "C"
    },
    {
        "prompt": "Which method is used to concatenate two lists in Python?",
        "options": ["A) append()","B) extend()","C) join()","D) concat()"],
        "answer": "B"
    },
    {
        "prompt": "What is the result of the expression: 10 % 3?",
        "options": ["A) 0","B) 1","C) 2","D) 3"],
        "answer": "B"
    },
    {
        "prompt": "What is the output of the following code: 'Hello, World!'.split(',')?",
        "options": ["A) ['Hello', 'World!']","B) ['Hello', ', World!']","C) ['Hello,', 'World!']","D) Error"],
        "answer": "A"
    },
    {
        "prompt": "Which data structure in Python uses the 'first in, first out' (FIFO) ordering?",
        "options": ["A) List","B) Stack","C) Queue","D) Set"],
        "answer": "C"
    },
    {
        "prompt": "What is the correct way to check if a key exists in a dictionary in Python?",
        "options": ["A) key in dictionary","B) dictionary.has_key(key)","C) dictionary[key] != None","D) Both A and C"],
        "answer": "D"
    },
    {
        "prompt": "What is the output of the following code: int('10') + 5?",
        "options": ["A) '105'","B) 105","C) 15","D) Error"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following is a valid Python comment?",
        "options": ["A) comment: This is a comment","B) // This is a comment","C) <!-- This is a comment -->","D) # This is a comment"],
        "answer": "D"
    },
    {
        "prompt": "What is the output of the following code: 'Python'[::-1]?",
        "options": ["A) 'Python'","B) 'nohtyP'","C) 'Pyt'","D) 'thon'"],
        "answer": "B"
    },
]

run_quiz(questions)