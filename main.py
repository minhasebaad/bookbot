from stats import get_text_length, character_count, sort_list
from printout import report
import sys


def get_book_text(filepath):
    contents = None
    with open(filepath, encoding="utf-8-sig") as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    book_path = sys.argv[1]
    print(len(sys.argv))
    
    book_content = get_book_text(book_path)
    text_length = get_text_length(book_content)
    dictionary = sort_list(character_count(book_content))
    report(book_path, text_length, dictionary)

main()
