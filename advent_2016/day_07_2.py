from day_07_1 import cut_string


def get_bab(aba):
    return aba[1] + aba[0] + aba[1]


def is_aba(aba):
    return aba[0] == aba[2] and aba[0] != aba[1]


def separate_different_ip_pieces(pieces):
    supernet_sequences = []
    hypernet_sequences = []
    for piece in pieces:
        if piece.startswith('['):
            hypernet_sequences.append(piece)
        else:
            supernet_sequences.append(piece)

    return supernet_sequences, hypernet_sequences


def find_aba_strings(input_string):
    abas = []
    for i in xrange(len(input_string) - 2):
        if is_aba(input_string[i:i+3]):
            abas.append(input_string[i:i+3])
    return abas


def supports_ssl(ip):
    supernet_sequences, hypernet_sequences = separate_different_ip_pieces(cut_string(ip))
    abas = find_aba_strings(''.join(supernet_sequences))
    for aba in abas:
        for item in hypernet_sequences:
            if get_bab(aba) in item:
                return True

    return False


