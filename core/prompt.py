from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator

questions = [
    {
        "type": "input",
        "message": "Enter the Project Title:",
        "validate": EmptyInputValidator(),
        "name": "title",
    },
    {
        "type": "rawlist",
        "message": "What drinks would you like to buy:",
        "default": 2,
        "choices": lambda result: ["Soda", "Cidr", "Water", "Milk"]
        if result["age"] < 18
        else ["Wine", "Beer"],
        "name": "drink",
    },
    {
        "type": "list",
        "message": "Would you like a bag:",
        "choices": ["Yes", "No"],
        "when": lambda result: result["drink"] in {"Wine", "Beer"},
    },
    {"type": "confirm", "message": "Confirm?", "default": True},

    {
        "type": "input",
        "message": "Provide the project author's name (can be a firm)",
        "validate": EmptyInputValidator(),
        "name": "author",
    },
]

result = prompt(questions=questions)