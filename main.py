from core.prompt import get_answers



def write_readme(data, filename="ReadMe-test.md"):
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {data['title']}\n\n")
        f.write(f"{data['description']}\n\n")
        
        f.write(f"## Installation\n")
        for line in data['installation'].splitlines():
            f.write(f"• {line}\n")
        f.write("\n")

        f.write(f"## Usage\n{data['usage']}\n\n")

        f.write(f"## License\n{data['license']}\n\n")
        
        if data['contribution'] == "Yes" and data['contributing_link']:
            f.write(f"## Contribution Guidelines\n")
            f.write(f"Please see ({data['contributing_link']}) for details on how you can contribute to the project.\n\n")

        f.write(f"## Author\n{data['author']}\n\n")

        f.write(f"## Contact\n")
        for line in data['contact'].splitlines():
            f.write(f"• {line}\n")
        f.write("\n")

        f.write(f"## Useful Links\n")
        for line in data['links'].splitlines():
            f.write(f"• {line}\n")

if __name__=="__main__":
    answers = get_answers()
    write_readme(answers)

