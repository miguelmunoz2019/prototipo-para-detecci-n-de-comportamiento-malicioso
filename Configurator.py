directory = ''


def main():
    path = r'config.txt'
    with open(path, 'r') as reader:
        directory = reader.readline().split(':')[1].strip()
        print(directory)


if __name__ == '__main__':
    main()
