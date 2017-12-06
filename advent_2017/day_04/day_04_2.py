from collections import Counter


def is_passphrase_valid(phrase):
    unique_words = set()
    letter_info = list()
    for word in phrase.split(' '):
        unique_words.add(word)
        letters = Counter(word)

        letter_info.append(letters)

    seen = list()
    all_sets_of_letters_unique = not any(i in seen or seen.append(i) for i in letter_info)
    all_words_unique = len(phrase.split(' ')) == len(unique_words)

    return all_words_unique and all_sets_of_letters_unique


def count_valid_passphrases(phrases):
    count = 0
    for phrase in phrases.splitlines():
        if is_passphrase_valid(phrase.strip()):
            count += 1
    return count


if __name__ == '__main__':
    print count_valid_passphrases("""aa bb cc
    dd ee dd""")
