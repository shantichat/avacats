import os
import time

import requests


def main(root, max_num):
    for i in range(max_num):
        image_path = f'{root}/{i}.jpg'
        if os.path.exists(image_path):
            print('-->', image_path, 'already exists')
            continue

        print('-->', image_path)
        r = requests.get('https://thiscatdoesnotexist.com')
        with open(image_path, 'wb') as f:
            f.write(r.content)

        time.sleep(2.5)


if __name__ == '__main__':
    main('source', 255)
