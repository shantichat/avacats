from zlib import crc32

import requests


class Avacat:
    def __init__(self, root='https://shantichat.github.io/avacats'):
        self.root = root
        self.info = requests.get(f'{root}/index.json').json()

    def __call__(self, name, size):
        assert size in self.info['sizes'], f"Size {size} not allowed, available sizes: {self.info['sizes']}"
        i = crc32(name.lower().encode()) % self.info['num']
        return f'{self.root}{size}x{size}/{i}.jpg'


if __name__ == '__main__':
    avacat = Avacat()
    print(avacat('alice@example.com', 80))  # https://shantichat.github.io/avacats80x80/171.jpg
    print(avacat('bob@example.com', 120))  # https://shantichat.github.io/avacats120x120/222.jpg
