def is_passphrase_valid(phrase):
    unique_words = set()
    for word in phrase.split(' '):
        unique_words.add(word)

    return len(phrase.split(' ')) == len(unique_words)

def count_valid_passphrases(phrases):
    count = 0
    for phrase in phrases.splitlines():
        if is_passphrase_valid(phrase.strip()):
            count += 1
    return count


if __name__ == '__main__':
    print count_valid_passphrases("""aa bb cc
    dd ee dd""")
