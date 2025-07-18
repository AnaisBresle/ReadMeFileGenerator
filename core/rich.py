from rich import Console
from rich import Panel  # bordered boxes for content
from rich import Syntax  # higlighter

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

