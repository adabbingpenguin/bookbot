import sys
from stats import get_total_word_count
from stats import count_book_characters
from stats import sort_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
    
        book = sys.argv[1]

        book_text = get_book_text(book)
        total_word_count = get_total_word_count(book_text)
        individual_word_count = count_book_characters(book_text)
        sorted_character_count = sort_character_count(individual_word_count)

        #report print

        print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {total_word_count} total words\n--------- Character Count -------\n")
        for dictionary in sorted_character_count:
            print(f"{dictionary["count"]}: {dictionary["amount"]}")

        print("============= END ===============") 
        

main()
