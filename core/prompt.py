from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator

questions = [
    {
        "type": "input", # single line text input
        "message": "Enter the Project Title:",
        "validate": EmptyInputValidator(),
        "name": "title",
    },
   
    {
        "type": "editor",  # multiline input in editor
        "name": "description",
        "message": "Enter the Project Description:"
    },
    {
        "type": "editor",
        "name": "installation",
        "message": "Enter Installation Instructions:"
    },
    {
        "type": "editor",
        "name": "usage",
        "message": "Describe how to use this project and what are the expected outputs."
    },
  
    {
        "type": "input",
        "name": "author",
        "message": "Author Name:",
        "validate": EmptyInputValidator(),
    },
    {
        "type": "input",
        "name": "contact",
        "message": "Contact Information (email, website, etc.):"
    }
]

result = prompt(questions=questions)