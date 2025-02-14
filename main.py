

def sort_char(dict):
    return dict["count"]  # This is all this function should do!

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):

    char_counts = {}
    file_contents = file_contents.lower()
    
    for char in file_contents:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    # This part should be in char_count, not in sort_char
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_char)
    return char_list

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        
    print(f"--- Begin report of {path_to_file} ---")
    
    count = word_count(file_contents)  # Call word_count() first
    print(f"{count} words found in the document")
    print()
    
    char_count_result = char_count(file_contents)
    for item in char_count_result:
        print(f"The '{item['char']}' character was found {item['count']} times")

if __name__ == "__main__":
    main()