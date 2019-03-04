def odd_chars(str1, str2):
    dict = set()

    for i in range(0, len(str1)):
        feed_dictionary(dict, str1[i])
        feed_dictionary(dict, str2[i])

    return dict


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    dict = odd_chars(str1, str2)

    if len(dict) == 0:
        return True

    return False


def feed_dictionary(dict, char):
    if char in dict:
        dict.discard(char)
    else:
        dict.add(char)


if __name__ == '__main__':
    original = 'ROMA'
    test = ['ROMAR', 'AMOR', 'MARO', 'ORAM', 'CATO', 'RONA', 'AAMR', 'AMRO     ', 'OMARR']

    for str2 in test:
        print(is_permutation(original, str2))
