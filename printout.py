
def report(path, length, dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for key in dictionary:
        if key.isalpha():
            print(f"{key}: {dictionary[key]}")
    print("============ END ============")
