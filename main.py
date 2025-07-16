from core.prompt import get_answers



def write_readme(data, filename="ReadMe-test.md"):
    
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in data.items():
            f.write(f"{key.upper()}:\n{value}\n\n")

if __name__=="_main_":
    answers = get_answers()
    write_readme(answers)

print(f"{filename} generated!")