def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = wordcount(text)
    char_list = character_count(text)

    
   
    # Displaying report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print(char_list)

# Takes text string (a book) and returns the number of words in string
def wordcount(book):
    words = book.split()

    return len(words)


def get_book_text(path):
     # open a file: 
    with open(path) as f:
        return f.read()

# Takes text string (a book) and returns the number of times each character appears in the string 
def character_count(book):
    characters = {}
    
    for c in book: 
        char = c.lower()

        if char in characters:
           characters[char] += 1
        else:
            characters[char] = 1

    return characters

if __name__ == "__main__":
    main()