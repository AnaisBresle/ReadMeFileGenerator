import markdown

class MarkdownWriter:
    def __init__(self,data):
        self.data = data

    def write_markdown(self, filename="ReadMe-test.md"):
    
        with open(filename, "w", encoding="utf-8") as f:
         f.write(f"# {self.data['title'].strip()}\n\n")
         f.write(f"## Description\n{self.data['description'].strip()}\n\n") ## Adding .strip to remove any blank space, breaks etc..
        
## Installation
         f.write(f"## Installation\n")
         for idx, line in enumerate(self.data['installation'].splitlines(), start=1):
           line = line.strip()
           if line:
                f.write(f"{idx}. {line}\n")
         f.write("\n")
       
## Usage
         f.write("## Usage\n")
         f.write(f"{self.data['usage'].strip()}\n\n")

## License & Contribution
         f.write("## License\n")
         f.write(f"{self.data['license'].strip()}\n\n")
        
         if self.data['contribution'] == "Yes" and self.data['contributing_link']:
            f.write(f"## Contribution Guidelines\n")
            link = self.data['contributing_link'].strip()
            f.write(f"[See CONTRIBUTING.md]({link}) for details on how to contribute.\n\n")

## Author & Contact
         f.write("## Author\n")
         f.write(f"{self.data['author'].strip()}\n\n")
 
         f.write(f"## Contact\n")
         for line in self.data['contact'].splitlines():
            line = line.strip()
            if line:
                f.write(f"• {line}\n")
            f.write("\n")
## Links
         f.write(f"## Useful Links\n")
         for line in self.data['links'].splitlines():
            line = line.strip()
            if line:
                f.write(f"• {line}\n")

    def convert_to_html (self, md_file="ReadME-test.md", html_file="ReadMe-Test.html"):
         with open(md_file, "r", encoding="utf-8") as f: # Open .md file in read mode
            content = f.read()
         html_content = markdown.markdown(content) # Convert the markdown to HTML tag using markdown module - convert ## ins h1, #h2 etc.. need to add inline css if want more fancy styles. 
         with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)   # create HTML file (write mode) 



