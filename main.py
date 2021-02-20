'''This module implements navigation on json file'''
import json

def read_data(path: str) -> list:
    '''Read information from json file'''
    try:
        with open(path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)

    except FileNotFoundError:
        print(f"Sorry, file from '{path}' isn't found")
        return None

    return data


def list_analysis(index: str, data: list):
    '''
    Return element of list with entered index if it exist
    >>> print(list_analysis('0', ['a', [2, 3], 'b', {'key': 345}]))
    a
    >>> print(list_analysis('1', ['a', [2, 3], 'b', {'key': 345}]))
    [2, 3]
    >>> list_analysis('all', ['a', [2, 3], 'b', {'key': 345}])
    a
    [2, 3]
    b
    {'key': 345}
    '''
    if index == 'all':
        for element in data:
            print(element)
        return None

    try:
        index = int(index)
        data = data[index]

    except (IndexError, ValueError):
        print(f'Sorry, there isn\'t element with index {index}')
        return None

    return data


def dict_analysis(user_key: str, data: list):
    '''
    Return element of dict with entered key if it exist
    >>> print(dict_analysis('a', {'a': [2, 3], 'b': 8}))
    [2, 3]
    >>> dict_analysis('all', {'a': [2, 3], 'b': 8})
    a: [2, 3]
    b: 8
    >>> dict_analysis('name', {'a': [2, 3], 'b': 8})
    Sorry, there isn't element with key 'name'
    '''
    if user_key == 'all':
        for key in data:
            print(f'{key}: {data[key]}')
        return None

    try:
        data = data[user_key]
    except KeyError:
        print(f"Sorry, there isn't element with key '{user_key}'")
        return None

    return data


def main():
    '''Main function'''
    path = input('Enter the path to json file: ')
    data = read_data(path)

    while data:
        if isinstance(data, list):
            print(f'This item is an array with {len(data)} elements')
            index = input('Enter index of element you want to see or "all" to see whole array: ')
            print()
            data = list_analysis(index, data)

        elif isinstance(data, dict):
            print('This item is an object with these keys:')
            for key in data:
                print(key)
            index = input('Enter key you want to see or "all" to see whole object: ')
            print()
            data = dict_analysis(index, data)

        else:
            print(data)
            return

if __name__ == '__main__':
    main()
