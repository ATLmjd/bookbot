def get_book_len(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(len(file_contents.split()))

def get_book_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        char_counts = {}
        file_contents_lc = file_contents.lower()
        for char in file_contents_lc:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        return(char_counts)

def sort_count_chars(in_dict):
    in_dict.sort(revers=True, key=sort_on)
    return(in_dict)