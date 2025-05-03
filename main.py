from stats import get_book_len,get_book_char_count,sort_count_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def main():
    num_words = get_book_len(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    word_dict = get_book_char_count(book_path)
    for char in word_dict.keys():
        if char.isalpha():
            print(f"{char}: {word_dict[char]}")

main()
