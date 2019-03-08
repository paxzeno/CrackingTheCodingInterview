internal_map = [[]] * 5


class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value


def calculate_index(key):
    return hash(key) % len(internal_map)


def put(key, value):
    index = calculate_index(key)
    entry = Entry(key, value)
    if len(internal_map[index]) == 0:
        internal_map[index] = [entry]
    else:
        internal_map[index].append(entry)
    return entry


def get(key):
    for entry in internal_map[calculate_index(key)]:
        if entry.key == key:
            return entry.value


if __name__ == '__main__':
    print(calculate_index('hi'))
    print(calculate_index('abc'))
    print(calculate_index('aa'))
    print(calculate_index('qs'))
    print(calculate_index('pl'))
    put('hi', 'man')
    put('abc', 'tastik')
    put('aa', 'chopstick')
    put('qs', 'clayface')
    put('pl', 'playdoh')
    print(internal_map)
    print(get('hi'))
    print(get('qs'))
    print(get('abc'))
    print(get('aa'))
    print(get('hi'))
    print(get('pl'))
    print(get('su'))
