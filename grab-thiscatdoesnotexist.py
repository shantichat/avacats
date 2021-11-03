import os
import time

import requests


def grab(root, max_num, *, pause=2.5):
    num = 0
    for i in range(max_num):
        image_path = f'{root}/{i}.jpg'
        if os.path.exists(image_path):
            print('-->', image_path, 'already exists')
            continue

        print('-->', image_path)
        r = requests.get('https://thiscatdoesnotexist.com')
        with open(image_path, 'wb') as f:
            f.write(r.content)
            num += 1
        time.sleep(pause)
    print('downloaded:', num)


if __name__ == '__main__':
    grab('source', 255)
