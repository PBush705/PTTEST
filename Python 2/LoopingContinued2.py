words_count = {}
words = input("Create a list of words").split()
biggest = ""
for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1
biggest = 0
for word in words_count:
    biggest = max(words_count.values())
    if words_count[word] == biggest:
        print(word)