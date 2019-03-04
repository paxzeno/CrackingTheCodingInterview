from string_permutation import feed_dictionary


def is_one_away(str1, str2):

    ## WRONG SOLUTION
    delta = len(str2) - len(str1)
    if delta > 1 or delta < -1:
        return False

    dict = set()
    for char in str1:
        feed_dictionary(dict, char)

    for char in str2:
        feed_dictionary(dict, char)

    if len(dict) > 2:
        return False

    return True


if __name__ == '__main__':
    input = [{'pale': 'ple'}, {'pales': 'pale'}, {'pale': 'bale'}, {'pale': 'bake'}, {'le': 'bale'}, {'bale': 'lal'},
             {'kibetch': 'kib3tch'}, {'lale': 'babe'}]
    for dict in input:
        for k, v in dict.items():
             print(is_one_away(k, v))
