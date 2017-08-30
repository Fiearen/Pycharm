def main():
    word_dict = {}
    sentence = str(input("Please write a sentence: "))
    words = sentence.split()
    for word in words:
        if word in word_dict:
            word_dict[str(word)] += 1
        else:
            word_dict[str(word)] = 1
    longest_word_len = longest_word(words)
    for word, count in sorted(word_dict.items()):
        print("{:<{}} = {}".format(word, longest_word_len, count))


def longest_word(words):
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
    return length


main()
