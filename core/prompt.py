from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator





questions = [
    {
        "type": "input", # single line text input
        "message": "Enter the Project Title:",
        "validate": EmptyInputValidator(),
        "name": "title",
        
    },
   
      inquirer.text(message="Provide a short description of the project:", multiline=True), # multiline input in editor
   
    {
        "type": "input",
        "name": "usage",
        "message": "Describe how to use this project and what are the expected outputs."
    },

     {
        "type": "input",
        "name": "installation",
        "message": "Enter Installation Instructions:"
    },

     {
        "type": "list",
        "name": "license",
        "message": "Choose a license:",
        "choices": [
            "No License — default copyright applies",
            "Unlicensed — no permissions granted",
            "Apache 2.0",
            "Boost Software License 1.0",
            "BSD 3-Clause",
            "GNU AGPLv3",
            "GNU GPLv2 (or later)",
            "GNU LGPLv3",
            "MIT",
            "Mozilla Public License 2.0",

        ],
        "default": "MIT"
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
        "message": "Contact Information (email, website, etc.):",
        "validate": EmptyInputValidator(),
    }
]

result = prompt(questions=questions)