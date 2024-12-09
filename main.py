def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = wordcount(text)
    char_list = character_count(text)

    char_list.sort(reverse=True, key=sort_on)

    # Displaying report
    print(f"--- Begin report of {book_path} ---\n")
    print(f"\t{word_count} words found in the document\n")
    for char in char_list:
        c = char["name"]
        count = char["count"]
        print(f"The '{c}' character was found {count} times")



# A function that takes a dictionary and returns the value of the "count" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

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

        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    # Convert list of dictionaries 
    char_list = [{"name": k, "count": v} for k, v in characters.items()]
    return char_list

if __name__ == "__main__":
    main()