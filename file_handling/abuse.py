# Read the data from the one file and check if the words are present in the another file 

base_file = './file_handling/base.txt'
target_file = './file_handling/demo.txt'
with open(base_file, 'r') as f:
    base_data = f.read()
    base_words = base_data.split()
    word_count = {word: 0 for word in base_words}

with open(target_file, 'r') as f:
    target_data = f.read()
    target_words = target_data.split()
    for word in target_words:
        if word.lower() in word_count:
            word_count[word.lower()] += 1

print(word_count)


