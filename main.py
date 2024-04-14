
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    cant_words = count_words(text)
    dict_characters = cant_characters(text)
    sorted_dictionary_list = chars_dict_to_sorted_list(dict_characters)

    print("--- Begin report of books/frankenstein.txt ---")
    print(cant_words, "words found in the document")
    for ch in sorted_dictionary_list:
        print(f"The {ch["char"]} character was found {ch["num"]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)


def cant_characters(text):
    lowercase_text = text.lower()

    dict_caracteres = {}
    for letra in lowercase_text:
        if letra in dict_caracteres:
            dict_caracteres[letra] = dict_caracteres[letra] + 1
        else:
            dict_caracteres[letra] = 1
    return dict_caracteres


def sort_on(a):
    return a["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if ch.isalpha() == True:
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()

