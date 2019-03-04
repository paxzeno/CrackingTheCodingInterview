def urlify(input, size):
    output = [None]*size
    for i in range(0, size):
        if input[i] == ' ':
            output[i] = '%20'
        else:
            output[i] = input[i]
    return ''.join(output)


if __name__ == '__main__':
    input = 'Mr John Smith '
    size = 13
    output = urlify(input, size)
    # expected Mr%20John%20Smith
    print(output)
