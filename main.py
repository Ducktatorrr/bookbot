def get_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def sort_char_dict(char_dict):
    char_list = []
    for c in char_dict:
        obj = {"char": c, "count": char_dict[c]}
        char_list.append(obj)

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def main():
    book = "books/frankenstein.txt"
    book_text = get_text(book)
    word_count = count_words(book_text)
    char_dict = count_characters(book_text)
    char_sorted_list = sort_char_dict(char_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()

    for i in char_sorted_list:
        if i["char"].isalpha():
            print(f"The '{i['char']}' character was found '{i['count']}' times")

    print("--- End report ---")


main()
