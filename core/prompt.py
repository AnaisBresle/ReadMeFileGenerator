from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator 

answers = {
    "title": inquirer.text(message="Enter the Project Title:", validate=EmptyInputValidator()).execute(),
    "description": inquirer.text(message="Provide a short description of the project:", multiline=True).execute(), 
    "usage": inquirer.text(message="Describe how to use this project and what are the expected outputs:", multiline=True).execute(),
    "installation": inquirer.text(message="Enter Installation Instructions (one step per line):", multiline=True).execute(),
    "license": inquirer.select (
        message="Choose a license:",
        choices= [
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
        default="MIT").execute(),
        "contribution": inquirer.select(
            message="Do you want to include a link to a CONTRIBUTING.md file?",
            choices=[
                "Yes",
                "No",
            ]).execute(),
            
    "author": inquirer.text(message="Author Name:", validate=EmptyInputValidator()).execute(),
    "contact": inquirer.text(message="Contact Information (email, website, etc. - (one info per line):",multiline=True, validate=EmptyInputValidator()).execute(),
    "links": inquirer.text(message="Useful Links:", multiline=True).execute(),
    }

# Ask for the CONTRIBUTING.md link only if they said "Yes"
if answers["contribution"] == "Yes":
    answers["contributing_link"] = inquirer.text(
        message="Provide the link to the CONTRIBUTING.md file:"
    ).execute()
else:
    answers["contributing_link"] = None


for key, value in answers.items():
    print(f"{key}: {value}")