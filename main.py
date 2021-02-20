import json

def read_data(path: str) -> list:
    '''Read information from json file'''
    with open(path, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def main():
    '''Main function'''
    path = input('Enter the path to json file: ')
    data = read_data(path)
    print(data)

# json_files/friends_list_AdamMGrant.json

if __name__ == '__main__':
    main()
