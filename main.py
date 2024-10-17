def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    counted_characters = {}
    lowered_book = book.lower()
    alphabet = list(map(chr, range(97, 123)))
    for letter in alphabet:
        count = lowered_book.count(letter)
        counted_characters[letter] = count
    return counted_characters

def sort_on(book_dict):
    return book_dict["number"]

def sort_dict(book_dict):
    sorted_dict = []
    for letter in book_dict:
        sorted_dict.append({"char": letter, "number": book_dict[letter]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

def print_report(path, book):
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(book)} words found in this book")
    print()
    counted_letters = sort_dict(count_characters(book))
    for letter in counted_letters:
        if not letter["char"].isalpha():
            continue
        print(f"The '{letter['char']}' character was found {letter['number']} times")
    print("--- End report ---")
    return

def main():
        book_path = "books/frankenstein.txt"
        book_text = get_book(book_path)
        print_report(book_path, book_text)
    

main()
