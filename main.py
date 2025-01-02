def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    words = word_counter(text)
    char_count = character_counter(text)
    sorted = sort_char_counts(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for entry in sorted:
        if entry["character"].isalpha():
            print(f"The '{entry['character']}' character was found {entry['count']} times")
    print("--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    return len(text.split())

def character_counter(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    char_list = [{"character": char, "count": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["count"], reverse=True)
    return char_list

main()
