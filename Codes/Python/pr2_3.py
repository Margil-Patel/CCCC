file_path = "try.txt"

with open(file_path, 'r') as file:
    text = file.read()
    words = text.split()
    words_count = len(words)
    print(words_count)