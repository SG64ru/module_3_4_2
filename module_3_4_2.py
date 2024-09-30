def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    #print(root_word)   # контроль

    for word in other_words:
        # print(word) # контроль
        word_lower = word.lower()
        # print(word_lower)# контроль

        if root_word in word_lower:
            same_words.append(word_lower)
        # print("в цикле ", same_words)
    return same_words


single_root_words("Disablement",  'Able', 'Mable', 'Disable', 'Bagel', 'Vsd')

print(single_root_words)


