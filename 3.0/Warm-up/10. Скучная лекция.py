if __name__ == "__main__":
    word = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dic = {}
    for letter in alphabet:
        alphabet_dic[letter] = 0
    length = len(word)
    for letter in range(len(word)):
        before = letter + 1
        after = length - before + 1
        alphabet_dic[word[letter]] += before*after
    for letter in alphabet:
        if alphabet_dic[letter] != 0:
            print(f"{letter}: {alphabet_dic[letter]}")
