def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = wordcount(text)

    print(word_count)



# Takes text string from book and returns integer number of words in string
def wordcount(book):
    words = book.split()

    return len(words)


def get_book_text(path):
     # open a file: 
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()