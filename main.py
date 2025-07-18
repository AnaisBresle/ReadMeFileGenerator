from core.prompt import get_answers
from core.markdown_writer import MarkdownWriter
from core.prettyfy import RichStyle
      

def main():
    # 1. Get data from user
    data = get_answers()

    # 2. Html convert
    htmlconvert = MarkdownWriter(data)
    htmlconvert.write_markdown()  

    # 3. Make MD file prettier
    prettyfy = RichStyle()
    prettyfy.display_markdown("README.md")

    print("\n ReadMe File created")

if __name__ == "__main__":
    main()

