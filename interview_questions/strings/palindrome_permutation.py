from string_permutation import feed_dictionary


def is_palindrome_possible(input):
    dict = set()

    for i in range(0, len(input)):
        if input[i] != ' ':
            feed_dictionary(dict, input[i].lower())

    return not len(dict) > 1


if __name__ == '__main__':
    input = 'Tact Coa'
    print(is_palindrome_possible(input))
    input = 'ROMA amor '
    print(is_palindrome_possible(input))
    input = 'PAL O A PIA'
    print(is_palindrome_possible(input))
    input = 'OMAR RAM O'
    print(is_palindrome_possible(input))
    input = 'PAL O A PLA'
    print(is_palindrome_possible(input))
