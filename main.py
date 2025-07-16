from core.prompt import get_answers



def write_readme(data, filename="ReadMe-test.md"):
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {data['title'].strip()}\n\n")
        f.write(f"## Description\n{data['description'].strip()}\n\n") ## Adding .strip to remove any blank space, breaks etc..
        
        f.write(f"## Installation\n")
        for line in data['installation'].splitlines():
            f.write(f"• {line}\n")
        f.write("\n")

        f.write("## Usage\n")
        f.write(f"{data['usage'].strip()}\n\n")

        f.write("## License\n")
        f.write(f"{data['license'].strip()}\n\n")
        
        if data['contribution'] == "Yes" and data['contributing_link']:
            f.write(f"## Contribution Guidelines\n")
            link = data['contributing_link'].strip()
            f.write(f"[See CONTRIBUTING.md]({link}) for details on how to contribute.\n\n")

        f.write("## Author\n")
        f.write(f"{data['author'].strip()}\n\n")

        f.write(f"## Contact\n")
        for line in data['contact'].splitlines():
            line = line.strip()
            if line:
                f.write(f"• {line}\n")
            f.write("\n")

        f.write(f"## Useful Links\n")
        for line in data['links'].splitlines():
            line = line.strip()
            if line:
                f.write(f"• {line}\n")

if __name__=="__main__":
    answers = get_answers()
    write_readme(answers)

