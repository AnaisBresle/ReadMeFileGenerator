from core.prompt import get_answers

def write_readme(answers, filename="ReadMe-test.md"):
    answers = get_answers()
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in answers.items():
            f.write(f"{key.upper()}:\n{value}\n\n")

    print(f"{filename} generated!")