
def sort_list(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

def get_text_length(content):
    words = []
    words = content.split()
    length = len(words)
    return length    

def character_count(content):
    character_dictionary = {}
    content = content.lower()
    for char in content:
        if not (char in character_dictionary):
            character_dictionary[char] = 1
        else:
            character_dictionary[char] += 1
    return character_dictionary
