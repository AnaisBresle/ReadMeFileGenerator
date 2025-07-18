from rich import Console
#from rich import Panel  # bordered boxes for content
#from rich import Syntax  # higlighter

class RichStyle:
    def __init__(self):
        self.console = Console()

    def _print_heading(self, line):  ## define how heading are styled
        heading = line.lstrip("#").strip()  # Remove '#' and blacnk space from md. markdown
        self.console.print(f"[bold]{heading}[/bold]")
        self.console.rule() ## nice hr type line to seperate 

    def _print_list(self, line):
        # Print list items with a bit of indent
        self.console.print(f"  {line.strip()}")

    def _print_link(self, line):
        # Print links in blue and underlined (simple style)
        self.console.print(f"[blue underline]{line.strip()}[/blue underline]")

    def display_markdown(self, filepath):
      
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:  # Read md  file line by line
                stripped = line.strip() # remove blank space
                
                # If the line starts with '#', it's a heading
                if stripped.startswith("#"):
                    self._print_heading(stripped)

                # If the line starts with '-' or '*' or is a numbered list item (e.g. "1. ")
                elif stripped.startswith(("-", "*")) or (len(stripped) > 2 and stripped[:2].isdigit() and stripped[2] == "."):
                    self._print_list(stripped)
                # If the line contains a markdown-style link [text](url) - This is how links are formatted in md files. 
                elif "[" in stripped and "](" in stripped:
                        self._print_link(stripped)
                else:
                    # For all other lines, print the text normally
                        self.console.print(stripped)
    