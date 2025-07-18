from rich import Console
from rich import Panel  # bordered boxes for content
from rich import Syntax  # higlighter

class RichStyle:
    def __init__(self):
        self.console = Console()

    def _print_heading(self, line):  ## define how heading are styled
        heading = line.lstrip("#").strip()  # Remove '#' and blacnk space from md. markdown
        self.console.print(f"[bold]{heading}[/bold]")
        self.console.rule()

    