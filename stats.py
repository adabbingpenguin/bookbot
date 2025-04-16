def get_total_word_count(book_text):
    split_text = book_text.split()
    return len(split_text)

    for word in book_text:
        total_count += 1
    return total_count

def count_book_characters(text):

    char_count = {}

    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["amount"]


def sort_character_count(character_count):
    list_of_dictionaries = []
    for count in character_count:
        individual_directory = {}
        if count == " ":
            continue
        else: 
            individual_directory["count"] = count
            individual_directory["amount"] = character_count[count]
            list_of_dictionaries.append(individual_directory)
    list_of_dictionaries.sort(reverse=True, key=sort_on)

    return list_of_dictionaries



