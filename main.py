def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(book_path, num_words, chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def find_max_index(chars_list):
    max_i = 0
    max_value = float('-inf')
    for i in range(0, len(chars_list)):
        if chars_list[i][1] > max_value:
            max_value = chars_list[i][1]
            max_i = i
    return max_i
    
def print_report(book_path, num_words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    chars_list = list(chars_dict.items())
    # print(chars_list)
    while len(chars_list) > 0:
        max_i = find_max_index(chars_list)
        if chars_list[max_i][0].isalpha():
            print(f"The '{chars_list[max_i][0]}' character was found {chars_list[max_i][1]} times")
        del chars_list[max_i]
    print("--- End report ---")

# def print_report(book_path, num_words, chars_dict):
#     print(f"--- Begin report of {book_path} ---")
#     print(f"{num_words} words found in the document")
#     chars_list = list(chars_dict.keys())
#     chars_list.sort()
#     for i in chars_list:
#         if i.isalpha():
#             print(f"The '{i}' character was found {chars_dict[i]} times")
#     print("--- End report ---")
main()